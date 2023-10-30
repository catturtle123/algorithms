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

int printCount;
int up;
int result;

void pick(int n, int count) {
    if (picked.size() == count) {
        int a = 0;
        rep(i, 0, picked.size()) a += picked[i];
        if(a == result) {
            printCount += 1;
        } 
        return;
    }

    for (int i = n + 1 ; i < up  ; i++) {
        picked.pb(o[i]); 
        pick(i, count); 
        picked.pop_back(); 
    }
}


int main() {
    FAST_IO;
    
    
    cin >> up;
    cin >> result;
    o.resize(up);
    rep(i, 0, o.size()) cin >> o[i];

    rep(i, 0, up) pick (-1, i + 1);
    cout << printCount << endl;
    
    
    return 0;
}