#!/usr/bin/env ruby

=begin
Finds all the circular primes below one million.
e.g. 197 -> 971 -> 719 are all primes.
=end

require 'Prime'

class String
  def rotate(n)
    new_string = self
    (1..n).each { |i| new_string = new_string[1..-1] + new_string[0] }
    new_string
  end
end

class Integer
  def is_circular_prime
    if not self.prime? then
      return false
    else
      self.length.times {|i| if not self.to_s.rotate(i).to_i.prime? then return false end }
      return true
    end
  end
end

primes_of_interest = Prime.take_while { |p| p < 10000000 }


