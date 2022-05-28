#!/usr/bin/perl
#
# Jump the user to WWW ImageMagick option manual
#
# A script is used as the location of 
#
$ENV{PATH} = '/bin:/usr/bin';

# Location of the option manual
# Eg option =  $URL.$JOIN."trim"
$URL = 'https://imagemagick.org/script/command-line-options.php';
$JOIN = '?#';

# Remove the indent of a here file...
# Adjust to suit you here file requirements
sub herefile {
  my $string = shift;
  $string =~ s/^\s+#.*\n//gm;  # completely remove full line comments
  $string =~ s/^\s+\| ?//gm;   # remove the indent part of the line
  $string =~ s/\s+$/\n/g;      # remove any extra end-of-line spaces
  return $string;
}

# Header of the HTML document
$header = herefile("
      | <HTML><HEAD>
      | <TITLE>IM v6 Option Reference Forwarder</TITLE>
      | </HEAD><BODY BGCOLOR=\"#BOC4DE\">
      | <DIV ALIGN=center>
      | <H1>IM v6 Option Reference Forwarder</H1>
      ");


if ( ($ENV{'QUERY_STRING'} || '') =~ /^[a-z-]*$/ ) {
  $option = $&;
  $URL .= $JOIN.$option if $ENV{'QUERY_STRING'};

  print herefile("
      | Location: $URL
      | Content-type: text/html
      |
      | $header
      |
      | Your browser failed to auto-jump to then<BR>
      | <A HREF=\"$URL\" >Manual for the command line option \"-$option\"</A>
      |
      ");
}
else {
  print herefile("
      | Content-type: text/html
      |
      | $header
      |
      | Forwarder was not given a valid option.<BR>
      | You can see all options on the <A HREF=\"$URL\"
      |  >IM Command Line Options</A> page.
      |
      ");
}

# Footer
print herefile("
      | </DIV></P>
      | <HR>
      | <ADDRESS>
      | Author: <A HREF=\"http://www.ict.griffith.edu.au/anthony/anthony.html\"
      |   >Anthony Thyssen</A>, &lt;Anthony.Thyssen&#64;gmail.com&gt;<BR>
      | </ADDRESS></BODY></HTML>
      ");

