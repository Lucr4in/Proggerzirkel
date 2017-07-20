import java.util.Arrays;
import java.util.Scanner;

public class main {


	public static boolean pruefenObElementschonInSortierenListe(int elementVar,int Liste[])
	{
		boolean rueckgabe = false;
		for(int i = 0;i <= Liste.length-1; i++) 
		{
			if(Liste[i] == elementVar)
			{
				rueckgabe = true;
			}
		}
		
		return rueckgabe;
	}
	
	public static boolean PruefenObListeSortiert(int listeWaggons[], int listeSortiert [])
	{
		boolean sortierung = true;
		
		for(int i=0;i <= listeWaggons.length-1;i++) 
		{
			if (listeWaggons[i] != listeSortiert[i]) 
			{
				sortierung = false;
			}
		}
		
		
		return sortierung;
	}
	
	public static void ContainerAufWaggonsSortieren(int listeContainer[],int listeWaggons[], int listeSortiert[]) {
		int pos = 0;
		int abbruch = 0;
		boolean ende = false;
				
		while (ende == false) 
		{
			ende = PruefenObListeSortiert(listeWaggons, listeSortiert);
			if (pruefenObElementschonInSortierenListe(listeContainer[pos],listeSortiert)) 
			{
				if ((pos+1) <= (listeContainer.length -1 )) {
					pos += 1;
				}
			}
			else 
			{
				listeSortiert[listeContainer[pos]-1] = listeContainer[pos];
				pos = listeContainer[pos] -1 ;
			}
			
			System.out.println("\n");
			System.out.println("*****Liste Sortiert*****");
			System.out.println(Arrays.toString(listeSortiert));
			System.out.println("*****Liste Container*****");
			System.out.println(Arrays.toString(listeContainer));
			System.out.println("*****Liste Waggons*****");
			System.out.println(Arrays.toString(listeWaggons));
			
			abbruch++;
			if (abbruch == 20) 
			{
			ende = true;
			}
		
		}
	}
	
	public static void main(String[] args) {
		
		//Input Scanner erzeugen und Anzahl an Containern einlesen
		Scanner user_input = new Scanner( System.in );
		System.out.println("Bitte geben Sie die Anzahl der Container ein: ");
		int containerAnzahl = user_input.nextInt();
		
		//Anlegen von Container und Waggon Array
		int[] waggonListe = new int[containerAnzahl];
		int[] containerListe = new int[containerAnzahl];
		int[] sortierteListe = new int[containerAnzahl];
	
		for (int i=0;i<containerAnzahl;i++)
		{
			
			containerListe[i] = i+1;
			waggonListe[i] = i+1;
			
		}

		
		ShuffleArray.shuffleArray(containerListe);
		user_input.close();
		
		ContainerAufWaggonsSortieren(containerListe,waggonListe,sortierteListe);
		
		System.out.println("Finished");
	}
}
