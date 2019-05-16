from pyknow import *

class PhConstan:
    ALCALINO = "ALCALINO"
    ACIDO = "ACIDO"
    LIGERAMENTE_ALCALINO ="LIGERAMENTE ALCALINO"
    LIGERAMENTE_ACIDO = "LIGERAMENTE ACIDO"
    NEUTRO = "NEUTRO"
    pass

class ElectriConstan:
    ALTA="ALTA"
    BAJA="BAJA"
    pass

class Suelo(Fact):
    pass


class reglasSuelo(KnowledgeEngine):
    @Rule (Suelo(ph=P(lambda ph: ph>7.2)))
    def rule0(self):
        print("\n\n\n")
        print("==> ph: ALCALINO")

    @Rule (Suelo(ph=P(lambda ph: ph<7.2)),Suelo(ph=P(lambda ph: ph>6.8)))
    def rule1(self):
        print("\n\n\n")
        print("==> ph: LIGERAMENTE ALCALINO")

    @Rule (Suelo(ph=P(lambda ph: ph<6.8)),Suelo(ph=P(lambda ph: ph>6.2)))
    def rule2(self):
        print("\n\n\n")
        print("==> ph: NEUTRO")

    @Rule(Suelo(ph=P(lambda ph: ph < 6.2)), Suelo(ph=P(lambda ph: ph > 5.6)))
    def rule3(self):
        print("\n\n\n")
        print("==> ph: LIGERAMENTE ACIDO")

    @Rule(Suelo(ph=P(lambda ph: ph < 5.6)))
    def rule4(self):
        print("\n\n\n")
        print("==> ph: ACIDO")

    @Rule(Suelo(ce=P(lambda ce: ce < 0.8)))
    def rule5(self):
        print("\n\n\n")
        print("==> conductividadElectrica: BAJA")

    @Rule(Suelo(ce=P(lambda ce: ce >= 0.8)))
    def rule6(self):
        print("\n\n\n")
        print("==> conductividadElectrica: ALTA")

    @Rule(Suelo(PH=PhConstan.ALCALINO))
    def rule7(self):
        print("\n\n\n")
        print("==> ExtractoSoluble: True")

    @Rule(Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO))
    def rule8(self):
        print("\n\n\n")
        print("==> ExtractoSoluble: True")

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),Suelo(PH=PhConstan.ALCALINO),Suelo(CE=ElectriConstan.ALTA))
    def rule9(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua");
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica");
        print("     |-(4) Acumulacion de iones alcalinoterreos	");

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)), Suelo(PH=PhConstan.ALCALINO), Suelo(CE=ElectriConstan.ALTA))
    def rule10(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.");

    @Rule(Suelo(limo=P(lambda limo: limo >= 50.0)), Suelo(PH=PhConstan.ALCALINO), Suelo(CE=ElectriConstan.ALTA))
    def rule11(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)");
        print("     |-(2) Suelo Hidromorfico");
        print("     |-(3) Limitaciones fisicas temporales");
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases");

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),Suelo(arena=P(lambda arena: arena <= 40.0)),Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)), Suelo(PH=PhConstan.ALCALINO), Suelo(CE=ElectriConstan.ALTA))
    def rule12(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)");
        print("     |-(2) Baja disponibilidad de Calcio");

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)), Suelo(PH=PhConstan.ALCALINO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule13(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua");
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica");
        print("     |-(4) Acumulacion de iones alcalinoterreos	");
        print("     |-(5) Baja disponibilidad de elementos menores ");

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)), Suelo(PH=PhConstan.ALCALINO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule14(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.");

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)), Suelo(PH=PhConstan.ALCALINO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule15(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)");
        print("     |-(2) Suelo Hidromorfico");
        print("     |-(3) Limitaciones fisicas temporales");
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(5) Baja disponibilidad de elementos menores ");

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),Suelo(arena=P(lambda arena: arena <= 40.0)), Suelo(PH=PhConstan.ALCALINO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule16(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)");
        print("     |-(2) Baja disponibilidad de Calcio");
        print("     |-(3) Baja disponibilidad de elementos menores ");

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
         Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule17(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua");
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica");
        print("     |-(4) Acumulacion de iones alcalinoterreos	");
        print("     |-(5) Alta saturación de calcio");
        print("     |-(6) Salinidad en el suelo");
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)");

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)),
         Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule18(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.");

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule19(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)");
        print("     |-(2) Suelo Hidromorfico");
        print("     |-(3) Limitaciones fisicas temporales");
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases");


    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule20(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)");
        print("     |-(2) Baja disponibilidad de Calcio");

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule21(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua");
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica");
        print("     |-(4) Acumulacion de iones alcalinoterreos	");
        print("     |-(5) Baja disponibilidad de elementos menores ");

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule22(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.");

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule23(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)");
        print("     |-(2) Suelo Hidromorfico");
        print("     |-(3) Limitaciones fisicas temporales");
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(5) Baja disponibilidad de elementos menores ");

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ALCALINO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule24(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)");
        print("     |-(2) Suelo Hidromorfico");
        print("     |-(3) Limitaciones fisicas temporales");
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(5) Baja disponibilidad de elementos menores ");

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla>=40.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule25(self):
        print("\n\n\n");

        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	");
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases");
        print("     |-(3) Salinidad en el suelo");


    @Rule(Suelo(arena=P(lambda arena: arena>= 50.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule26(self):
        print("\n\n\n");

        print("     |-(1) Revisar las mediciones realizadas.");

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule27(self):
        print("\n\n\n")

        print("     |-(1) Salinidad en el suelo")

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule28(self):

          print("\n\n\n")

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule29(self):
        print("\n\n\n")

        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Limitaciones de movimiento de agua")

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule30(self):
        print("\n\n\n")

        print("     |-(1) Coloraciones grises suelo (Glaizeado)")

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule31(self):
        print("\n\n\n")

        print("     |-(1) Coloraciones grises suelo (Glaizeado)")

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.NEUTRO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule32(self):
        print("\n\n\n")

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule33(self):
        print("\n\n\n")

        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule34(self):
        print("\n\n\n")

        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(Suelo(arena=P(lambda arena: arena >= 45.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule35(self):
        print("\n\n\n")

        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule36(self):
        print("\n\n\n")

    print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
    print("     |-(2) Baja disponibilidad de Calcio")



    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule37(self):
        print("\n\n\n")

        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")


    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 50.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule38(self):
        print("\n\n\n")

        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule39(self):
        print("\n\n\n")

        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.LIGERAMENTE_ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule40(self):
        print("\n\n\n")

    print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
    print("     |-(2) Baja disponibilidad de Calcio")
    print("     |-(3) Baja disponibilidad de elementos menores ")

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule41(self):
        print("\n\n\n")

        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Acumulacion de iones alcalinoterreos	")
        print("     |-(4) Salinidad en el suelo")
        print("     |-(5) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(6) Baja disponibilidad de Calcio")
        print("     |-(7) Contenido de Aluminio")

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule42(self):
        print("\n\n\n")

        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(Suelo(limo=P(lambda limo: limo >= 50.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule43(self):
        print("\n\n\n")

        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule44(self):
        print("\n\n\n")

        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    @Rule(Suelo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule45(self):
        print("\n\n\n")

        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(Suelo(arena=P(lambda arena: arena >= 50.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule46(self):
        print("\n\n\n")

        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(Suelo(limo=P(lambda limo: limo >= 45.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.BAJA))
    def rule47(self):
        print("\n\n\n")

        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(Suelo(limo=P(lambda limo: limo <= 40.0)),
          Suelo(arena=P(lambda arena: arena <= 40.0)),
          Suelo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
          Suelo(PH=PhConstan.ACIDO),
          Suelo(CE=ElectriConstan.ALTA))
    def rule48(self):
        print("\n\n\n")

        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")


engine = reglasSuelo()
engine.reset()
engine.declare(Suelo(ph=5, ce=0.8,PH=PhConstan.NEUTRO,arcilla=77,CE=ElectriConstan.ALTA,arena=30,limo=30))
engine.run()