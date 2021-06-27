#include "rna_transcription.h"
#include <map>

using namespace std;

namespace rna_transcription 
{
  map<char, char> DtoR_NA_map = 
  {
    { 'G', 'C' },
    { 'C', 'G' },
    { 'T', 'A' },
    { 'A', 'U' }
  };

  // function to convert char in DNA to corresponding RNA char as defined in map<>.
  char to_rna(char DNA) 
  {
    return DtoR_NA_map[DNA];
  }

  // for each nucleotide found in a given string of DNA
  // convert nucleotide from DNA to RNA by calling the above function to_rna()
  // then return modified DNA.
  string to_rna(string DNA) 
  {
    for (char nucleotide : DNA) 
    {
      nucleotide = to_rna(nucleotide);
    }
    return DNA;
  }
}
