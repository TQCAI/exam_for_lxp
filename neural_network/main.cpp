#include <bits/stdc++.h>
#include <bits/stdc++.h>
#define FF(a,b) for(int a=0;a<b;a++)
#define F(a,b) for(int a=1;a<=b;a++)
#define LEN 200
#define INF 1000000

using namespace std;
typedef long long ll;
const double pi=acos(-1);

int N,M;
ll x[LEN];
ll y[LEN];
ll b[LEN];
ll W[LEN][LEN];

int main()
{
    freopen("../nn_data/Test01.in","r",stdin);
    scanf("%d%d",&N,&M);
    FF(i,N)
        scanf("%lld",&x[i]);
    FF(i,M)
        FF(j,N)
            scanf("%lld",&W[i][j]);
    FF(i,M)
        scanf("%lld",&b[i]);
    FF(i,M){
        ll sum=0;
        FF(j,N){
            sum+=W[i][j]*x[j];
        }
        y[i]=sum+b[i];
    }
    FF(i,M){
        printf("%d",y[i]);
        if(i!=M-1)
            printf(" ");
    }
    return 0;
}




