#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
import os
from math import exp

BDD_path = "./bddprofil"  #chemin vers la base de donnee de profil
RESULTS_path="./resultat5x"  #chemin vers le dossier des resultats à analyser
fileIn=sys.argv[1]  # argument 1 : fichier à utiliser

class Profil(object):  #object profil
    def __init__(self,line,indicePosition): #prend en argument une ligne d'un reportsorted en argument et la position de la ligne
        line=line.split(".")
        if len(line)!=2:
            raise ValueError  # ligne de taille anormale
        else:
            self.jonction=line[0][-2:].lower()  #nom de la jonction
            self.nbReads=int(line[1].split(' ')[1].strip())  #nombre reads alignes sur cette jonction
            self.rang=indicePosition #position de la jonction dans le fichier

    def __str__(self)
        res = []
        for _attr in self.__dict__:
            res.append(_attr + " : " + str(self.__dict__[_attr]))
        return "\n".join(res)

    def __repr__(self):
        return str(self)

class Allele(object): #object allele
    def __init__(self,line):
        line=line.strip().split(' ')
        if len(line)!=2:
            raise ValueError  # ligne de taille anormale
        else:
            self.name=line[0]  #nom allele
            self.sequenceMotif=line[1] #sequence des motifs associé à l'allele

    def __str__(self):
        allele = []
        for _attr in self.__dict__:
            allele.append(_attr + " : " + str(self.__dict__[_attr]))
        return "\n".join(allele)

    def __repr__(self):
        return str(self)

class Genotype(object):   #object genotype
    def __init__(self,nom):
            self.name=nom.upper()  #mettre le nom des genotype en majuscule
            self.distance=0 #initialisation de la valeur de distance

    def __str__(self):
        allele = []
        for _attr in self.__dict__:
            allele.append(_attr + " : " + str(self.__dict__[_attr]))
        return "\n".join(allele)

    def __repr__(self):
        return str(self)


#construction du dictionnaire des alleles à partir fichier motifAllele.txt
#permet de construire l'object Allele
f=open('motifAllele.txt','r')
motifAllele={}
for line in f:
    motifAllele[line.strip().split(' ')[0]]=line.strip().split(' ')[1]
f.close()

#construction dictionnaire occurence à partir du fichier occurenceMotif.txt
#implementer pour des potentiels tentatives de ponderation en fonction du nombre occurence des motifs dans les jonctions
f=open('occurenceMotif.txt','r')
occurenceMotif={}
for line in f:
    occurenceMotif[line.strip().split(' ')[0]]=int(line.strip().split(' ')[1])
f.close()

def constructObjetProfil(file): #construction du profil de l'individu XX à partir du fichier reportsortedIndivXX
    res=[]
    n = 1
    for line in file:
        res.append(Profil(line,n)) #profil stocke dans une liste
        n+= 1
    return res

def constructObjetAllele():#construction de la liste d'object alleles
    f=open('motifAllele.txt','r')
    motifAllele=[]
    for line in f:
        motifAllele.append(Allele(line))
    return motifAllele


def cpteurReads(listeProfil): #compte le nombre total de reads d'un profil permet de normaliser les valeurs
    total=0
    for i in range(len(listeProfil)): #parcours la liste qui stocke le profil
        total+=listeProfil[i].nbReads #somme le nombre de reads
    return total

def ponderationJonction(jonction,k=2): #fonction pour ponderer le poids d'une jonction
    """
    Voici toutes les tentatives de ponderation utilisées malheureusement infructueuses
    """
    #ponderation=1/(1+exp(100-15*occurenceMotif[jonction]))
    #ponderation=1/(1+exp(100-20*occurenceMotif[jonction]))
    #ponderation=1/(1+exp(100-30*occurenceMotif[jonction]))
    #ponderation=1/(1+exp(150-30*occurenceMotif[jonction]))
    #ponderation=1/(1+exp(5-0.8*occurenceMotif[jonction]))
    #ponderation=1/occurenceMotif[jonction]
    #ponderation=1/(1+exp(5-0.5*occurenceMotif[jonction]))
    return ponderation

#permet de calculer la distance entre le profil XX et tous les profils de la base de donnee, return le profil le plus proche du profil XX
def divergentProfils(listeRes): #listeRes -> profil XX
    genotype=[]
    k=0 #indice de l'haplotype
    for path, dirs, files in os.walk(BDD_path): #parcours la base de données
        for fileProfilGenotype in files:
            name=fileProfilGenotype.split('.')[0][12:] #recupere le nom du genotype de la BDD
            genotype.append(Genotype(name)) #liste de génotype testé
            profilFile=open(BDD_path+'/'+fileProfilGenotype,'r') #ouverture du fichier profil à tester
            profilGenotype=constructObjetProfil(profilFile)  #construction de l'object profil à partir du fichier de profil
            sommeReadsGenotype=cpteurReads(profilGenotype) #total des reads alignés sur le profil à tester
            sommeReadsXX=cpteurReads(listeRes) #total des reads alignés sur le profil XX
            for i in range(len(profilGenotype)):
                for j in range(len(listeRes)):
                    if profilGenotype[i].jonction==listeRes[j].jonction:
                        a=profilGenotype[i].nbReads/sommeReadsGenotype #
                        b=listeRes[j].nbReads/sommeReadsXX
                        difference=a-b #distance entre le profilA et le profilB pour la jonction Y
                        #tentatives de ponderations
                        #difference=ponderationJonction(listeRes[j].jonction)*a-b
                        #difference=(listeRes[j].rang-profilGenotype[i].rang)*ponderationJonction(listeRes[j].jonction)*a-b
                        #difference=float((listeRes[j].rang-profilGenotype[i].rang)/10)*a-b
                        #difference=listeRes[j].rang*(a-b)
                        genotype[k].distance+=abs(difference) #somme des distances pour toutes les jonctions
            k+=1
    genotype=sorted(genotype, key=lambda x: x.distance) score#trie la liste de genotype en fonction de la distance
    return genotype[0].name#premier genotype de la liste donc avec la plus petite distance


fResults=open(RESULTS_path+'/'+fileIn,'r')
profilXX=constructObjetProfil(fResults) #construction du profil de l'individu XX
print (str(divergentProfils(profilXX)))#affiche le profil le plus probable
