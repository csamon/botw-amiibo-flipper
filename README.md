# Flipper Zero - Playlists Amiibo pour Zelda Breath of the Wild

Playlists NFC pour le **Flipper Zero**, optimisees pour les recompenses amiibo dans **The Legend of Zelda: Breath of the Wild**.

Chaque fichier `.nfc` apparait dans **une seule playlist**. Aucun doublon.

---

## Structure

```
playlists/
  ZELDA-COFFRES.txt    # 38 amiibo Zelda (coffres + items exclusifs)
  AUTRES-BOUFFE30.txt  # 30 amiibo non-Zelda (nourriture generique)
```

---

## Installation sur le Flipper Zero

1. Copie le contenu du depot **[FlipperAmiibo](https://github.com/Gioman101/FlipperAmiibo)** dans `/ext/nfc/FlipperAmiibo-main/` sur ta carte SD
2. Copie les fichiers `.txt` du dossier `playlists/` dans `/ext/nfc/playlists/` (ou l'emplacement de ton app NFC Playlist)
3. Installe l'app **NFC Playlist** depuis le Flipper App Hub
4. Navigue vers la playlist et lance-la

---

## Regles importantes dans BotW

| Regle | Detail |
|---|---|
| **1 scan par jour par amiibo** | Cooldown 24h, reset a minuit (horloge Switch) |
| **Reset horloge** | Couper internet Switch > Parametres > Heure > avancer de 24h |
| **Save-scum** | Sauvegarder AVANT le scan, recharger si mauvais drop |
| **Pity system** | Apres ~5 scans sans rare, le prochain est garanti dans le pool rare |
| **Parapente requis** | Pool de loot limite tant que le parapente n'est pas obtenu |
| **Bete Divine requise** | Il faut liberer au moins 1 Bete Divine pour debloquer les items exclusifs |

---

## ZELDA-COFFRES.txt - 38 amiibo

**Tous les amiibo Zelda qui donnent des coffres avec recompenses.** A scanner en priorite chaque jour.

Les premiers de la liste sont les plus importants (items uniques introuvables ailleurs dans le jeu).

### Items exclusifs (introuvables autrement)

| Amiibo | Recompense exclusive | Notes |
|---|---|---|
| SSB Zelda (x3 UIDs) | **Arc Crepuscule** | Meilleur arc du jeu, portee infinie, fleches lumiere illimitees |
| SSB Link (x3 UIDs) | **Epona** (1er scan) | Cheval stats max (5/5/5) - enregistrer en ecurie immediatement ! |
| Wolf Link MAX / 20H / 3H | **Compagnon Wolf Link** | Invocable plusieurs fois/jour, chasse et attaque automatiquement |
| Guardian | **Fleches Anciennes** | Seule source quotidienne renouvelable, one-shot les Guardians |
| Link Majora's Mask | **Set Fierce Deity + Epee** | Meilleure armure d'attaque du jeu |
| 4 Champions | **Casques Divins** | Ancient Proficiency (+80% degats) avec l'Armure Ancienne |
| Link Twilight Princess | **Set Crepuscule** | Set d'armure exclusif |
| Link Skyward Sword | **Set du Ciel + Epee de la Deesse** | Set d'armure exclusif |
| OoT Link | **Set du Temps + Epee Biggoron** | Set d'armure exclusif |
| Wind Waker Link | **Set des Vents + Boomerang** | Set d'armure exclusif |
| 8-Bit Link | **Set du Heros** | Set d'armure exclusif |
| Sheik (x2 UIDs) | **Masque de Sheik** | Vitesse nocturne |
| Ganondorf (x2 UIDs) | Royal/Knight Claymore | Armes haut-tier fiables |
| Toon Link (x2 UIDs) | Set des Vents + **meilleur drop poisson** | Hearty Salmon, Staminoka Bass |
| Young Link (x2 UIDs) | Set du Temps (variante) | Set d'armure |
| Link Rider | **Selle + Bride du Voyageur** | Cosmetique cheval exclusif |
| Link Archer | Royal/Knight Bow | Bons arcs + nourriture |
| Bokoblin | Clubs + pieces monstre | Ingredients pour elixirs |
| Zelda BotW | Arcs + plantes | Plantes pour cuisine |
| Wind Waker Zelda | Meilleur drop plantes | Armoranth, Swift Carrot, Blue Nightshade |
| Zelda & Loftwing | Herbes variees | Plantes |
| Link's Awakening | Items generiques | Zelda-universe mais pas d'exclusif BotW |
| TotK Link / Zelda / Gerudo King | Items generiques | Amiibo post-BotW, reconnus comme Zelda |

### Astuces

- **Epona** : invoquee une seule fois par sauvegarde. Si elle meurt sans etre enregistree, elle est perdue
- **Wolf Link** : pas soumis au cooldown quotidien, invocable plusieurs fois par jour
- **3 fichiers Zelda SSB** = 3 chances par jour pour l'Arc Crepuscule (chaque UID est independant)
- **Casques Divins** : portes avec l'Armure Ancienne complete (2 etoiles+), ils donnent le bonus Ancient Proficiency

---

## AUTRES-BOUFFE30.txt - 30 amiibo

**Amiibo non-Zelda** : chacun donne 3-4 ingredients de cuisine aleatoires (champignons, pommes, viande, herbes...). Pas de coffre.

> Datamining confirme : tous les amiibo non-Zelda utilisent la meme table de loot (`Item_Amiibo_DropTable_Common`). Aucun n'est meilleur qu'un autre. L'interet est d'en scanner beaucoup = plus de piles de nourriture gratuite.

| # | Franchise | Amiibo |
|---|---|---|
| 1-8 | Super Mario | Mario, Luigi, Peach, Bowser, Yoshi, Toad, Donkey Kong, Boo |
| 9-10 | Super Mario 30th | Classic Mario, Modern Mario |
| 11-13 | Splatoon | Inkling Boy, Inkling Girl, Octoling Boy |
| 14-15 | Kirby | Kirby, Meta Knight |
| 16-17 | Fire Emblem | Chrom, Alm |
| 18 | Mega Man | Mega Man |
| 19 | Pikmin | Pikmin |
| 20 | Dark Souls | Solaire of Astora |
| 21 | Diablo | Loot Goblin |
| 22 | Pokemon | Detective Pikachu |
| 23 | Chibi-Robo | Chibi-Robo |
| 24 | Box Boy | Qbby |
| 25 | Super Mario Cereal | Super Mario Cereal |
| 26 | Pokken Tournament | Shadow Mewtwo |
| 27 | Shovel Knight | Shovel Knight |
| 28 | Metroid | Samus (Dread) |
| 29 | Monster Hunter | Palamute |
| 30 | Animal Crossing | Isabelle |

> 30 amiibo x 3-4 items = **~100 ingredients gratuits par jour** pour la cuisine.

---

## Ordre de scan quotidien

```
1. ZELDA-COFFRES     <- toujours, sans exception (coffres + items exclusifs)
2. AUTRES-BOUFFE30   <- si besoin de nourriture en masse
```

---

## Fichiers speciaux decouverts dans le depot

| Fichier | Particularite |
|---|---|
| `Wolf_Link_20_Heart.nfc` | Wolf Link modifie avec **20 coeurs** |
| `Wolf_Link_MAX_LEVEL.nfc` | Wolf Link au **niveau maximum** |

---

*Genere avec [Claude Code](https://claude.ai/claude-code) - base sur le depot [FlipperAmiibo by Gioman101](https://github.com/Gioman101/FlipperAmiibo)*
