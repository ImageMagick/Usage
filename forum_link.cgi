#!/usr/bin/perl
#
# Jump the user to WWW ImageMagick option manual
#
$ENV{PATH} = '/bin:/usr/bin';

# Location of the option manual
# Eg   location = $URL.$USER."u=1163"
$URL = 'https://legacy.imagemagick.org/discourse-server/';
$FORUM = 'viewforum.php?';
$TOPIC = 'viewtopic.php?';
$USER = 'memberlist.php?mode=viewprofile&';

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
      | <TITLE>IM Forum Forwarder</TITLE>
      | </HEAD><BODY BGCOLOR=\"#BOC4DE\">
      | <DIV ALIGN=center>
      | <H1>IM Forum Forwarder</H1>
      ");


if ( ($ENV{'QUERY_STRING'} ) =~ /^f=\d+$/ ) {
  $URL .= $FORUM.$&;

  print herefile("
      | Location: $URL
      | Content-type: text/html
      |
      | $header
      |
      | Your browser failed to auto-jump to the right
      | <A HREF=\"$URL\" >IM Forum Page</A>
      |
      ");
}
elsif ( ($ENV{'QUERY_STRING'} ) =~ /^(f=\d+&)?t=\d+$/ ) {
  $URL .= $TOPIC.$&;

  print herefile("
      | Location: $URL
      | Content-type: text/html
      |
      | $header
      |
      | Your browser failed to auto-jump to the right
      | <A HREF=\"$URL\" >IM Forum Page</A>
      |
      ");
}
elsif ( ($ENV{'QUERY_STRING'} ) =~ /^(f=\d+&)?(t=\d+&)?p=(\d+)$/ ) {
  $URL .= $TOPIC."$1$2p=$3#p$3";

  print herefile("
      | Location: $URL
      | Content-type: text/html
      |
      | $header
      |
      | Your browser failed to auto-jump to the right
      | <A HREF=\"$URL\" >IM Forum Page</A>
      |
      ");
}
elsif ( ($ENV{'QUERY_STRING'} ) =~ /^u=\d+$/ ) {
  $URL .= $USER.$&;

  print herefile("
      | Location: $URL
      | Content-type: text/html
      |
      | $header
      |
      | Your browser failed to auto-jump to the right
      | <A HREF=\"$URL\" >Users profile</A>
      |
      ");
}
else {
  print herefile("
      | Content-type: text/html
      |
      | $header
      |
      | Forum Link was not given a recognised option. -- ABORTING
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

