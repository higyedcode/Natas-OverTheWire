#! /usr/bin/perl

# print "Hello there perl student!\n";
# print "What is your favourite hacking webiste? \n";

# $name = <STDIN>;
# chomp $name;

# print "Thanks! $name is my favourite too ! \n";

# system("neofetch");




# Check for the correct number of command-line arguments
if (@ARGV != 1) {
    die "Usage: $0 <filename>\n";
}

my $filename = $ARGV[0];

# Open the file for reading
open(my $filehandle, $filename) or die "Could not open file '$filename' for reading: $!";

# Read and print the contents of the file
while (my $line = <$filehandle>) {
    print $line;
}

# Close the file
close($filehandle);

exit 0;

