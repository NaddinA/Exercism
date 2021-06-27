#include "hamming.h"
#include <stdexcept>

namespace hamming {

  int compute(std::string s, std::string t)
  {
    // Error Check
    if (s.length() != t.length())
    {
      throw std::domain_error("The two strands must be equal in length\n");
    }
    
    int ham_dist = 0;
    for (int i = 0; (unsigned)i < s.length(); i++)
    {
      ham_dist += s[i] != t[i];
    }
    return ham_dist;
  }
}
