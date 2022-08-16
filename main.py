print("**********************************************")
print("calculadora de formulas de física e matematica")
print("**********************************************")
escolha = int(input("qual calculadora usar?\n  [1] matematica   [2] física\n"))

if escolha == 1:
    print(" Essa é a minha calculadora de pitagoras!\n ")
    print("a formula de pitágoras é A²= B²+ C²\n ")
    co = float(input("qual é o valor do cateto oposto?\n"))
    ca = float(input("qual é o valor do cateto adjacente?\n"))
    print("o valor da hipotenusa é", ((ca**2) + (co**2))*1/2)