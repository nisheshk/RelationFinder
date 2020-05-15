# Relation Finder

Imagine you would like to know how you are related to your father's mother brother's sister's daughter's son.
Woow I know its not easy, especially not for me.

So, I have prepared the script that finds the relation between two individuals. I have used BFS shortest path algorithm that figures out the shortest relation path between two individuals.

How to run the project?

<ul>

<li> You need to make entries in family_import.txt </li>
<li> The entries should be in the following format.<br/>

```
A,Mother,B
```

It means A is the mother of B
</li>
<li> The allowed relation types are Mother, Father, Husband and Wife</li>
<li> For the Husband/Wife entry. If you make an entry:

```
A,Husband,B #Then you don't have to add B,Wife,A
```
</li>
<li> Sample family_import.txt file is present. Do check it out.</li>
<li> Your python version should be >=3.6</li>
<li> Run the script relation_finder2.py.</li>

<br/>
Now when some distant relatives comes to your house to pay a visit. ask the relatives name and find how he/she is related to you using this script.
But be careful, because there should be an entry of that relative in the file family_import.txt
