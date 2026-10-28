# ----------------------------------------------------------------------
# C1. Saraksta kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar sešiem skaitļiem. Izvadi to skaitu, summu, vidējo, lielāko un mazāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā skaitļus, nosauc ar vārdu vertibu_kopa.


a=[9,8,12,42,50,60]
vertibu_kopa = []

x=len(a)
b=sum(a)
c=sum(a)/len(a)
n=min(a)
m=max(a)
vertibu_kopa.append(x)
vertibu_kopa.append(b)
vertibu_kopa.append(c)
vertibu_kopa.append(n)
vertibu_kopa.append(m)

print(vertibu_kopa)
