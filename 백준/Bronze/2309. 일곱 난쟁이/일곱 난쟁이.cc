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

vector<int> s;
vector<int> picked;
vector<bool> visited;
int finish;

void pick() {
    if(picked.size() == 7) {

        if (finish == 1) {
            return;
        }

        int sum = 0;

        rep(i, 0, picked.size()) sum += picked[i];
        
        if(sum == 100) {
            sort(picked.begin(), picked.end());
            rep(i, 0, picked.size()) cout << picked[i] << endl;
            finish = 1;
        } 
        
        return;
    }

    for(int i = 0; i < 9; i++) {
        if(visited[i]) continue;
        visited[i] = true;
        picked.push_back(s[i]);
        pick();
        visited[i] = false;
        picked.pop_back();
    }
}

int main(void) {
    FAST_IO;   
    s.resize(9);
    visited.resize(9);
    rep(i, 0, 9) cin >> s[i];
    pick();
    return 0;
}