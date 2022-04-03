embed
<drac2>
trinket_table = get_gvar("203cc488-ee1c-4d75-8bd5-01c6f3bbcbd5")
trinkets = [line.strip() for line in trinket_table.strip().splitlines()]
rolled = roll("1d100")
trinket = trinkets[rolled - 1]
</drac2>
-title "Trinket hunt!"
-desc "You go out looking for trinkets and find `{{trinket}}`".
-f "Your roll|`{{rolled}}`|inline"
-footer "Trinket table | PHB 160-161"
