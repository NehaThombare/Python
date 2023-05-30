import java.util.Scanner;

public class Selection{
    public static void main(String args[])
    {
        int n,i,j,temp;
        int arr[]=new int[50];

        Scanner sc=new Scanner(System.in);
        System.out.println("Enter how many numbers do you want: ");
        n=sc.nextInt();

        System.out.println("Enter"+n+"elements:");
        for(i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println("Sorting Array using selection sort:");
        for( i=0;i<n;i++){
            for(j=i+1;j<n;j++){
                if(arr[i]>arr[j]){
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
        System.out.println("Array after sorting:");
        for(i=0;i<n;i++)
        {
            System.out.println(arr[i]+" ");
        }
    }
}