#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0; i<(n); ++i)
using ll = long long;

int main(){
    int Q;
    cin >> Q;
    queue<ll> q;
    ll now = 0;

    rep(qi,Q){
        int type;
        cin >> type;
        if(type == 1){
            q.push(now);
        }
        if(type==2){
            ll t;
            cin >> t;
            now+=t;
        } 
        if (type==3){
            int ans=0;
            ll h;
            cin >> h;
            while(q.size() && now - q.front() >= h){
                ans++;
                q.pop();
            }
            cout << ans << "\n";
        }

    }


}