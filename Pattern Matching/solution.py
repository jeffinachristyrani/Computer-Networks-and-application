#include <stdbool.h>
#include <string.h>

bool isMatch(const char* s, const char* p) {
    int p_len = strlen(p);
    int star_idx = -1;
    
    for (int i = 0; i < p_len; i++) {
        if (p[i] == '*') {
            star_idx = i;
            break;
        }
    }
    
    int left_len = star_idx;
    int right_len = p_len - star_idx - 1;
    int s_len = strlen(s);
    int first_left = -1;
    
    for (int i = 0; i <= s_len - left_len; i++) {
        if (strncmp(s + i, p, left_len) == 0) {
            first_left = i;
            break;
        }
    }
    
    if (first_left == -1) {
        return false;
    }
    
    for (int i = s_len - right_len; i >= first_left + left_len; i--) {
        if (strncmp(s + i, p + star_idx + 1, right_len) == 0) {
            return true;
        }
    }
    
    return false;
}
