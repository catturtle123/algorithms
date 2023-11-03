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

int cache[501][501];
int triangle[501][501];
vector<int> line;

int main(void) {
    FAST_IO;   
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            cin >> triangle[i][j];
        }
    }

    for (int i = 1; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            if (j == 1) {
                cache[i][j] = triangle[i][j] + cache[i - 1][j];
            } else if (j > 1 && j < i) {
                cache[i][j] = max(triangle[i][j] + cache[i - 1][j], triangle[i][j] + cache[i - 1][j - 1]);
            } else {
                cache[i][j] = triangle[i][j] + cache[i - 1][j - 1];
            }
            
        }
    }

    for (int i = 0; i <= n ; i++) {
        line.pb(cache[n][i]);
    }

    sort(line.begin(), line.end());

    cout << line[n] << endl;
    return 0;
}