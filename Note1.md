# Note \#1

You find a sheet of paper on an enemy you've yet to encounter. It says the following:

> **Practice ciphers!**  
>  
> From demo --  
> 'dog'  
> Key 'a' -> 004015007    
> Key 'dog' -> 0380999055  
> Let's try it ... key 'dog'  
> dog=4,15,7 -> 4\*1+15\*2+7\*3 = ~~52~~ 55  
> 4+15+7=26 \*3= ~~81~~ 78
>  
> *what the fuck is a log?*  
> log<sub>10</sub>(k\*10<sup>n</sup>) = log<sub>10</sub>(k/10)+n+1 <-- what's that small 10 for?  
> apparently the first thing is about:  
> 1-x=k/10 -> 10-10x=k -> 10-k = 10x -> **1-k/10 = x**
>  
>> So the whole 'log' thing is   
>> -( (1-k/10) + (1-k/10)<sup>2</sup>/2 + (1-k/10)<sup>3</sup>/3 )\*.4343 + n + 1<-- the bastards
>  
> 78=7.8\*10<sup>1</sup> so k=7.8 and n=1  
> -( (1-.78) + (1-.78)<sup>2</sup>/2 + (1-.78)<sup>3</sup>/3 )\*.4343 + 1 + 1 =  
> -(.22+.22<sup>2</sup>/2 + .22<sup>3</sup>/3)\*.4343 + 2 =  
> 2-0.248\*0.4343=2-.108=1.89, now round it down --> 1  
> 10<sup>1</sup>=10 so 55/10=5.5 <-- I hate math  
> so factor = 5.5.
> Rotate the letters by the length of the key = 3. *Remember to wrap around if it goes around*
> (4+3)\*5.5=38.5, (15+3)\*5.5=99, (7+3)\*5.5 = 55  
> Round down, make 3 numbers  
> **038 099 055** <-- Success!  
> Key a?  
> 1\*1=1, 1=1\*10<sup>0</sup>, so -( .9+.9<sup>2</sup>/2+.9<sup>3</sup>/3)\*.4343+0+1 = 1-.67=0.32 -> 0  
> So 10<sup>0</sup>=1 so 1/1=1 so (4+1)\*1, (15+1)\*1, (7+1)\*1 --> **005 016 008** <-- haha! maybe I can do math
>  
> Remember space is 27, period 28, question 29.
>  
> Memo: remember the elder everlasting  
>  
> Test for real:  
> 'dog' with real key is --> 037003043  
> 'ercrain' with real key is --> 039009036009032047001  
> Draft message:  
>> 018039026005053032001026013003026045047013026013045039026039001036053032017039011  
>> 018039026018047053053026032013013032036051026003001026054047037011015054054039009011026039017039  
>> 047013026047011026047054005003009013032001013026013003026013045039047009026005053032001011028026037003026001003013026041032047053028


He also has one other sheet of paper on him. It's far less marked up and much more succinct.


> The younger as he is  
> 064023039029064004004039048055039052011009055041
