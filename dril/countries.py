"""Country codes and groupings for Latin America and the Caribbean.

ISO 3166-1 alpha-3 codes; subregions follow the UN M49 standard (Caribbean,
Central America including Mexico, South America). Spanish names are the forms
used in ECLAC source files. All projects use this table; do not keep private copies.
"""
import pandas as pd

# iso3, Spanish name as in ECLAC files, English name, M49 subregion
_ROWS = [
    ("ATG", "Antigua y Barbuda", "Antigua and Barbuda", "Caribbean"),
    ("ARG", "Argentina", "Argentina", "South America"),
    ("BHS", "Bahamas", "Bahamas", "Caribbean"),
    ("BRB", "Barbados", "Barbados", "Caribbean"),
    ("BLZ", "Belice", "Belize", "Central America"),
    ("BOL", "Bolivia", "Bolivia (Plurinational State of)", "South America"),
    ("BRA", "Brasil", "Brazil", "South America"),
    ("CHL", "Chile", "Chile", "South America"),
    ("COL", "Colombia", "Colombia", "South America"),
    ("CRI", "Costa Rica", "Costa Rica", "Central America"),
    ("CUB", "Cuba", "Cuba", "Caribbean"),
    ("DMA", "Dominica", "Dominica", "Caribbean"),
    ("DOM", "República Dominicana", "Dominican Republic", "Caribbean"),
    ("ECU", "Ecuador", "Ecuador", "South America"),
    ("SLV", "El Salvador", "El Salvador", "Central America"),
    ("GRD", "Granada", "Grenada", "Caribbean"),
    ("GTM", "Guatemala", "Guatemala", "Central America"),
    ("GUY", "Guyana", "Guyana", "South America"),
    ("HTI", "Haití", "Haiti", "Caribbean"),
    ("HND", "Honduras", "Honduras", "Central America"),
    ("JAM", "Jamaica", "Jamaica", "Caribbean"),
    ("MEX", "México", "Mexico", "Central America"),
    ("NIC", "Nicaragua", "Nicaragua", "Central America"),
    ("PAN", "Panamá", "Panama", "Central America"),
    ("PRY", "Paraguay", "Paraguay", "South America"),
    ("PER", "Perú", "Peru", "South America"),
    ("KNA", "Saint Kitts y Nevis", "Saint Kitts and Nevis", "Caribbean"),
    ("VCT", "San Vicente y las Granadinas", "Saint Vincent and the Grenadines", "Caribbean"),
    ("LCA", "Santa Lucía", "Saint Lucia", "Caribbean"),
    ("SUR", "Suriname", "Suriname", "South America"),
    ("TTO", "Trinidad y Tabago", "Trinidad and Tobago", "Caribbean"),
    ("URY", "Uruguay", "Uruguay", "South America"),
    ("VEN", "Venezuela", "Venezuela (Bolivarian Republic of)", "South America"),
]

COUNTRIES = pd.DataFrame(_ROWS, columns=["iso3", "name_es", "name_en", "subregion"])

# Spellings found in source files that differ from the ECLAC standard form.
_ALIASES = {"Trinidad y Tobago": "Trinidad y Tabago", "Belize": "Belice", "Haiti": "Haití",
            "Mexico": "México", "Peru": "Perú", "Panama": "Panamá", "Brazil": "Brasil"}


def iso3(name_es: str) -> str:
    """ISO3 code for a Spanish country name; raises KeyError for unknown names."""
    name = _ALIASES.get(name_es.strip(), name_es.strip())
    hit = COUNTRIES.loc[COUNTRIES.name_es == name, "iso3"]
    if hit.empty:
        raise KeyError(f"unknown country name: {name_es!r}")
    return hit.iloc[0]
