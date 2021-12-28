/*input
Juliana BonecaDaMinnie
Jessica Flor
Mariana QuebraCabeca
Jean PapelCrepom
Joao BolaDeVolei
JulioCesar Livros
Emma Livros
Julius Carteira
-- --
Mariana
Jean
Julius
Joana
Jessica
Juliana
Adelar
Elaine
*/
#include <bits/stdc++.h>
using namespace std;


int main(){
	string name, gift;
	map<string, string> list;
	map<string, string>::iterator it;

	while(cin>>name>>gift){
		if(!name.compare("--") && !gift.compare("--")){
			break;
		}else{
			list[name] = gift;
		}
	}

	while(cin>>name){
		it = list.find(name);
		if(it != list.end()){
			cout << "Child: " << name << endl;
			cout <<  "Gift " << list[name] << endl;
		}else{
			cout << "404 not found" << endl;
		}
		cout << endl;
	}

	return 0;
}