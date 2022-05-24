#include <stdio.h> 

int isprime(int n){
    int flag = 0;
    
    if(n == 0 || n == 1){
        flag = 1;
    } 
    else if(n<0){
        flag = 1;
    }
    
    for(int i=2;i<=n/2;i++){
        if(n%i==0){
            flag = 1;
            break;
        }
    }
    
    if(flag==0){
        return 1;
    }
    else {
        return 0;
    }
}

int main()
{   
    int t;
    scanf("%d",&t);

while(t--){
    int n,num1,num2,temp1,temp2=0;
    scanf("%d",&n);
    
    for(int i=2;i<10000;i++){
        if(isprime(i)){
            int temp = n-i;
            if(isprime(temp)){ 
                temp1 = temp - i;
                if(temp1>temp2){
                    num1 = i;
                    num2 = temp;
                    temp2 = temp - i;
                }
            }
        }
    }  
    
    int sum = (num2+num1); 
    
    if(sum==n)
    printf("%d %d\n",num1,num2); 
    else 
    printf("-1 -1\n");
   
}
    return 0;
}
