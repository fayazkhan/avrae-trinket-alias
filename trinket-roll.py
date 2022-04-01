embed
<drac2>
trinket_table = get_gvar("203cc488-ee1c-4d75-8bd5-01c6f3bbcbd5")
trinket_dict = [line.strip() for line in trinket_table.strip().splitlines()]
trinket = trinket_dict[roll("1d100") - 1]
</drac2>
-title "You found {{trinket}}"
