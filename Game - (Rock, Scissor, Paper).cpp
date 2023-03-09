#include <iostream>
#include <stdlib.h>
#include <ctime>

using namespace std;
int main(){

    int random,choice;
    string name;

    srand(time(0));

    cout<<"\n========== GAME ROCK SCISSOR PAPER ==========\n"<<endl;
    cout<<"Input player name\t : ";cin>>name;
    cout<<"\n========== HAVE A NICE PLAY =========="<<endl;
    cout<<"\nOptions"<<endl;
    cout<<"(1). Rock"<<endl;
    cout<<"(2). Scissor"<<endl;
    cout<<"(3). Paper"<<endl;
    cout<<"\nInput your choice : ";cin>>choice;
    cout<<endl;

    random = (rand()%3)+1;

    if(choice == 1){
        cout<<"your choice\t : Rock"<<endl;
        if(random == 1){
            cout<<"computer choice\t : Rock"<<endl;
            cout<<"(DRAW)"<<endl;
        }
        else if(random == 2){
            cout<<"computer choice\t : Scissor"<<endl;
            cout<<"(You WIN)"<<endl;
        }
        else{
            cout<<"computer choice\t : Paper"<<endl;
            cout<<"(You LOSE)"<<endl;
        }
    }
    else if(choice == 2){
        cout<<"your choice\t : Scissor"<<endl;
        if(random == 1){
            cout<<"computer choice\t : Rock"<<endl;
            cout<<"(You LOSE)"<<endl;
        }
        else if(random == 2){
            cout<<"computer choice\t : Scissor"<<endl;
            cout<<"(DRAW)"<<endl;
        }
        else{
            cout<<"computer choice\t : Paper"<<endl;
            cout<<"(You WIN)"<<endl;
        }
    }
    else if(choice == 3){
        cout<<"your choice\t : Paper"<<endl;
        if(random == 1){
            cout<<"computer choice\t : Rock"<<endl;
            cout<<"(You WIN)"<<endl;
        }
        else if(random == 2){
            cout<<"computer choice\t : Scissor"<<endl;
            cout<<"(You LOSE)"<<endl;
        }
        else{
            cout<<"computer choice\t : Paper"<<endl;
            cout<<"(DRAW)"<<endl;
        }
    }
    else{
        cout<<"Invalid choice"<<endl;
    }

return 0;
}
