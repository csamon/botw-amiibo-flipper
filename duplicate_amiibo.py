"""
Duplicate amiibo .nfc files with randomized UIDs for Flipper Zero.
Each unique UID = separate 24h cooldown in BotW = more scans per day.

Usage: python duplicate_amiibo.py [--copies N] [--source-dir DIR] [--output-dir DIR]
"""

import os
import re
import random
import argparse
import shutil


def generate_uid():
    """Generate a valid NTAG215 UID (7 bytes, starts with 04)."""
    # Byte 0 is always 0x04 for NXP manufacturer
    uid = [0x04] + [random.randint(0x00, 0xFF) for _ in range(6)]
    return uid


def compute_bcc0(uid):
    """BCC0 = 0x88 XOR UID[0] XOR UID[1] XOR UID[2]"""
    return 0x88 ^ uid[0] ^ uid[1] ^ uid[2]


def compute_bcc1(uid):
    """BCC1 = UID[3] XOR UID[4] XOR UID[5] XOR UID[6]"""
    return uid[3] ^ uid[4] ^ uid[5] ^ uid[6]


def uid_to_str(uid):
    return " ".join(f"{b:02X}" for b in uid)


def modify_nfc_file(content, new_uid):
    """Replace UID, Page 0, Page 1, and Page 2 BCC1 in .nfc file content."""
    bcc0 = compute_bcc0(new_uid)
    bcc1 = compute_bcc1(new_uid)

    # Replace UID line
    content = re.sub(
        r"^UID:.*$",
        f"UID: {uid_to_str(new_uid)}",
        content,
        flags=re.MULTILINE,
    )

    # Replace Page 0: UID[0] UID[1] UID[2] BCC0
    page0 = f"Page 0: {new_uid[0]:02X} {new_uid[1]:02X} {new_uid[2]:02X} {bcc0:02X}"
    content = re.sub(r"^Page 0:.*$", page0, content, flags=re.MULTILINE)

    # Replace Page 1: UID[3] UID[4] UID[5] UID[6]
    # Keep the last byte (SAK/internal) from original if present
    page1_match = re.search(r"^Page 1: .. .. .. (..)$", content, flags=re.MULTILINE)
    last_byte = page1_match.group(1) if page1_match else "80"
    page1 = f"Page 1: {new_uid[3]:02X} {new_uid[4]:02X} {new_uid[5]:02X} {last_byte}"
    content = re.sub(r"^Page 1:.*$", page1, content, flags=re.MULTILINE)

    # Replace BCC1 in Page 2 (first byte only, keep rest)
    page2_match = re.search(
        r"^Page 2: .. (..) (..) (..)$", content, flags=re.MULTILINE
    )
    if page2_match:
        page2 = f"Page 2: {bcc1:02X} {page2_match.group(1)} {page2_match.group(2)} {page2_match.group(3)}"
        content = re.sub(r"^Page 2:.*$", page2, content, flags=re.MULTILINE)

    return content


# Files to duplicate: the most valuable amiibo that only have 1 copy
TARGETS = {
    # TOP priority - unique exclusive rewards, only 1 file each
    "Legend_of_Zelda/BOTW/Guardian.nfc": "Guardian",
    "Legend_of_Zelda/BOTW_June/Link_Majora_s_Mask.nfc": "Majoras_Mask",
    "Legend_of_Zelda/BOTW_Champions/Daruk.nfc": "Daruk",
    "Legend_of_Zelda/BOTW_Champions/Mipha.nfc": "Mipha",
    "Legend_of_Zelda/BOTW_Champions/Urbosa.nfc": "Urbosa",
    "Legend_of_Zelda/BOTW_Champions/Rivali.nfc": "Revali",
    # Armor sets - only 1 file each
    "Legend_of_Zelda/BOTW_June/Link_Twilight_Princess.nfc": "TP_Link",
    "Legend_of_Zelda/BOTW_June/Link_Skyward_Sword.nfc": "SS_Link",
    "Legend_of_Zelda/30th_Anniversary/Ocarina_Of_Time_Link.nfc": "OoT_Link",
    "Legend_of_Zelda/30th_Anniversary/Wind_Waker_Link.nfc": "WW_Link",
    "Legend_of_Zelda/30th_Anniversary/8_Bit_Link.nfc": "8bit_Link",
    "Legend_of_Zelda/BOTW/Link_Archer.nfc": "Archer",
    "Legend_of_Zelda/BOTW/Link_Rider.nfc": "Rider",
    "Legend_of_Zelda/BOTW/Bokoblin.nfc": "Bokoblin",
    "Legend_of_Zelda/BOTW/Zelda.nfc": "BotW_Zelda",
}


def main():
    parser = argparse.ArgumentParser(
        description="Duplicate amiibo .nfc files with new UIDs"
    )
    parser.add_argument(
        "--copies",
        type=int,
        default=2,
        help="Number of copies per file (default: 2)",
    )
    parser.add_argument(
        "--source-dir",
        default=r"C:\Users\clem-\OneDrive\Bureau\amiibo\FlipperAmiibo-main\FlipperAmiibo-main",
        help="Source directory with .nfc files",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory (default: _DUPLICATES inside source dir)",
    )
    args = parser.parse_args()

    output_dir = args.output_dir or os.path.join(args.source_dir, "_DUPLICATES")
    os.makedirs(output_dir, exist_ok=True)

    all_generated = []

    for rel_path, short_name in TARGETS.items():
        src = os.path.join(args.source_dir, rel_path)
        if not os.path.exists(src):
            print(f"SKIP (not found): {rel_path}")
            continue

        with open(src, "r", encoding="utf-8") as f:
            original = f.read()

        for i in range(1, args.copies + 1):
            new_uid = generate_uid()
            new_content = modify_nfc_file(original, new_uid)
            out_name = f"{short_name}_clone{i}.nfc"
            out_path = os.path.join(output_dir, out_name)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            all_generated.append((out_name, uid_to_str(new_uid)))
            print(f"OK: {out_name} (UID: {uid_to_str(new_uid)})")

    # Generate playlist lines
    print(f"\n--- Generated {len(all_generated)} files in {output_dir} ---")
    print("\nPlaylist lines (add to ZELDA-COFFRES.txt):")
    for name, _ in all_generated:
        print(f"/ext/nfc/FlipperAmiibo-main/_DUPLICATES/{name}")


if __name__ == "__main__":
    main()
