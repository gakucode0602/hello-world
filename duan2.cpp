#include<iostream>
#include<cstdlib>
#include<string>
#include<ctime>
using namespace std;
void menu()
{
    cout << "***************************" << endl;
    cout << "* NHAP LUA CHON CUA BAN   *" << endl;
    cout << "* [1]. NHAP SAN PHAM.     *" << endl;
    cout << "* [2]. TIM SAN PHAM       *" << endl;
    cout << "* [3]. XUAT DON HANG      *" << endl; 
    cout << "***************************" << endl;
}

// MA SAN PHAM THU NHAT SS (SAMSUNG)
// MA SAN PHAM THU HAI AP (APPLE)

// HANG 1
typedef struct SAMSUNG
{
    string tensanpham;
    char masanpham;
    int soluong;
    double dongia;   
} ss ;

// HANG 2
typedef struct APPLE
{
    string tensanpham,madongsanpham;
    char masanpham;
    int soluong;
    double dongia ;
} ap;

void nhapdonhang(ss *a,int n)
{
    cout << "NHAP THONG TIN SAN PHAM CHO " << n << " DON HANG " << endl;
    cout << "MA SAN PHAM SAMSUNG " << endl;
    for(int i = 0;i<n;i++)
    {
        cout << "NHAP SAN PHAM THU " << i+1 << endl;
        cin.ignore(); 
        cout << "NHAP TEN SAN PHAM : ";getline(cin,a[i].tensanpham);
        //cout << "MA SAN PHAM : ";
        cout << "NHAP SO LUONG DONG MAY : ";cin >> a[i].soluong;
        cout  << "NHAP GIA BAN CHO DONG MAY : ";cin >> a[i].dongia;
    }
}

void nhapdonhang(ap *a,int n)
{
    cout << "NHAP THONG TIN SAN PHAM CHO " << n << " DON HANG " << endl;
    cout << "MA SAN PHAM SAMSUNG " << endl;
    for(int i = 0;i<n;i++)
    {
        cout << "NHAP SAN PHAM THU " << i+1 << endl;
        cin.ignore(); 
        cout << "NHAP TEN SAN PHAM : ";getline(cin,a[i].tensanpham);
        //cout << "MA SAN PHAM : ";
        cout << "NHAP SO LUONG DONG MAY : ";cin >> a[i].soluong;
        cout  << "NHAP GIA BAN CHO DONG MAY : ";cin >> a[i].dongia;
    }
}

int main()
{
    system("cls");
    // NHAP SAMSUNG
    int n;cout << "Nhap so luong san pham SAMSUNG ban muon nhap ve : ";cin >> n;
    ss *a = new ss[n];
    nhapdonhang(a,n);
    cout << "\n";
    // NHAP IPHONE
    int m;cout << "Nhap so luong san pham IPHONE ban muon nhap ve : ";cin >> m;
    ap *b = new ap[n];
    nhapdonhang(b,m);
    return 0;
}