# Denne filen inneholder skjelettet til Praktisk Øving 0 i faget TDT4160
# Kopier filen inn i Ripes-simulatoren, enten lokalt eller på ripes.me
# Selve oppgaven skal løses i området markert med ###############
# Når du er ferdig trykker du "Run".
# Sjekk at programmet fullfører, og at output ser ut som du forventer.
# Hvis alt ser bra ut kan du levere løsningen din på INGInious.
# Kopier KUN teksten innenfor ################-området!
# Når du leverer vil INGInious teste løsningen, og rapportere om eventuelle feil.

# I denne øvingen skal du skrive assembly som tar inn to tall, og regner ut summen
# Input ligger i registrene a1 og a2
# Output skal legges i register a0

# Setup av input
li a1, 7
li a2, 34

########################################################################################
# Skriv din kode her

add a0, a1, a2

########################################################################################

# Print verdien i register a0 som et heltall
li a7, 1
ecall

# Exit med kode 0
li a7, 10
ecall
