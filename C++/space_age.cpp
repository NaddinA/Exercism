#include "space_age.h"

namespace space_age 
{
  static constexpr double earth_year_in_seconds = 31557600.0;
  static constexpr double mercury_year_in_earth_years = 0.2408467;
  static constexpr double venus_year_in_earth_years = 0.61519726; 
  static constexpr double mars_year_in_earth_years = 1.8808158;
  static constexpr double jupiter_year_in_earth_years = 11.862615;
  static constexpr double saturn_year_in_earth_years = 29.447498;
  static constexpr double uranus_year_in_earth_years = 84.016846;
  static constexpr double neptune_year_in_earth_years = 164.79132;

  long long space_age::seconds() const { return GivenSecs; }

  double space_age::on_earth() const 
  { return GivenSecs / earth_year_in_seconds; }
  double space_age::on_mercury() const 
  { return on_earth() / mercury_year_in_earth_years; }
  double space_age::on_venus() const 
  { return on_earth() / venus_year_in_earth_years; }
  double space_age::on_mars() const 
  { return on_earth() / mars_year_in_earth_years; }
  double space_age::on_jupiter() const 
  { return on_earth() / jupiter_year_in_earth_years; } 
  double space_age::on_saturn() const 
  { return on_earth() / saturn_year_in_earth_years; }
  double space_age::on_uranus() const 
  { return on_earth() / uranus_year_in_earth_years; }
  double space_age::on_neptune() const 
  { return on_earth() / neptune_year_in_earth_years; }
}
