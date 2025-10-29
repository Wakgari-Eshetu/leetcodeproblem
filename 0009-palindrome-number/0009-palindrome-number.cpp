class Solution {
public:
    bool isPalindrome(int x) {
       if(x<0){
        return false;
       } 
        long int reverse=0,remiender;
        long int originalx=x;
       while(x>0) 
    { 
        remiender=x%10;
        
        reverse=reverse*10+remiender;
        x=x/10;
    }
    if(originalx==reverse){
        return true;
    }
    else{
        return false;
    }
    }
};