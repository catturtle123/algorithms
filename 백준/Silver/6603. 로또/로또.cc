#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define rrep(i, a, b) for(auto i = a; i > b; --i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define RREP(i, a, b) for(auto i = a; i >= b; --i)
#define pii pair<int, int>
#define tii tuple<int, int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define PIV (1 << 20)
using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;
 
vector<int> picked; 
vector<int> o;

int up;

void pick(int n) {
    if (picked.size() == 6) {
        rep(i, 0, picked.size()) cout << picked[i] << ' ';
        cout << endl;
        return;
    }

    for (int i = n + 1 ; i < up  ; i++) {
        picked.pb(o[i]); 
        pick(i); 
        picked.pop_back(); 
    }
}


int main() {
    FAST_IO;
    
    while (true){
        cin >> up;
        if (up == 0) {
            break;
        }
        o.resize(up);
        rep(i, 0, o.size()) cin >> o[i];
        pick (-1);
        cout << endl;
    }
    
    return 0;
}