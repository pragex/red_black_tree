/* 
 * Create by Richard Savard
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include "htree.h"


int
main(int argc, char * argv[])
{	
  printf("*** C VERSION %ld ***\n", __STDC_VERSION__);

  htree tree;

  htree_init(&tree);

  
  htree_cleanup(&tree);
  
  return EXIT_SUCCESS;
}

