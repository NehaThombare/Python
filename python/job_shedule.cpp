#include <bits/stdc++.h>
using namespace std;

//structure for holding values
typedef struct Job
{
    int jobNum;
    int deadline;
    int profit;
}Job;

bool compare(Job a, Job b);
void jobSequencing(Job input[], int n);

int main()
{
    int n;
    cout<<"enter the no of jobs";
    cin >> n;
    Job input[n];
    // inputing the values
    for (int i = 0; i < n; i++)
    {	cout<<"enter the job number";
        cin >> input[i].jobNum;
        cout<<"enter the deadline or time";
        cin >> input[i].deadline;
        cout<<"enter the profit";
        cin >> input[i].profit;
    }

    jobSequencing(input, n);
}

// a custom comparison function for arrenging jobs in decreasing order of profit
bool compare(Job a, Job b)
{
    return (a.profit > b.profit);
}

// main part of code where job sequencing happens
void jobSequencing(Job input[], int n)
{
    sort(input, input + n, compare);

    int result[n];
    
    bool slot[n];
    // setting all values in slot as false
    memset(slot, 0, sizeof(slot));

    for (int i = 0; i < n; i++)
    {
        for (int j = min(n, input[i].deadline)-1; j >= 0; j--)
        {
            if(slot[j] == false)
            {
                result[j] = i;
                slot[j] = true;
                break;
            }
        }
    }

    cout << "Job sequenced in order: ";
    for (int i=0; i<n; i++)
    {
       if (slot[i] == true)
        cout << input[result[i]].jobNum << " ";
    }
}
// #Bakery Chatbot
// from nltk.chat.util import Chat, reflections

// pairs =[
// 	['my name is (.*)', ['Hello % 1']],
// 	['(hi|hello|hey|hola|ni hao|konichiwa)', ['Hey there! Welcome to Foodies Bakery! How can I help you?']],
// 	['(.*) your name', ['My name is Washington!']],
// 	['(.*)do you do', ['I help to clear doubts with respect to the restaurant & your service.']],
// 	['(.*)dishes(.*)|(.*)menu(.*)', ['We offer sandwiches, cupcakes, rolls, tea, hot cocoa, noodles.']],
// 	['(.*)types of noodles', ['We have vegetarian and chicken noodles.']],
// 	['(.*)types of sandwiches', ['We have chutney and mayo sandwiches.']],
// 	['(.*)types of rolls', ['We have vegetarian and tandoori rolls.']],
// 	['(.*)types of tea', ['We have black, green, white and brick tea.']],
// 	['(.*)types of cupcakes', […