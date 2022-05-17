#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int test_case;
	cin>>test_case;
	while(test_case--){
	    long int no_of_ele_in_set , mean_of_set , min , max;
	    cin>>no_of_ele_in_set>>mean_of_set;
	    long int set[no_of_ele_in_set];
	    for(int i =0 ; i<no_of_ele_in_set ;i ++){
	        cin>>set[i];
	    }
	    min = set[0] ;
	    max = set[0] ;
	    for(int i =1 ; i<no_of_ele_in_set ;i ++){
	        if(min > set[i]){
	            min = set[i];
	        }
	        if(max < set[i]){
	            max = set[i];
	        }
	    }
	    if(min <= mean_of_set && max >= mean_of_set){
	        cout<<"Yes"<<endl;
	    }
	    else{
	        cout<<"No"<<endl;
	    }
	    
	    
	}
	return 0;
}
