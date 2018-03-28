/* 
 * Create by Richard Savard
 */


#ifndef HTREE_H
#define HTREE_H

#ifdef __cplusplus
extern "C"
{
#endif

#include <stddef.h>

#ifndef CUSTOM_THASH_TYPE
typedef int thash;
#endif

struct hnode {
  thash hash;
  int red;
  struct node * left;
  struct node * right;
  char str[];
};

struct {
  hnode * head;
  size_t count;
} htree;

extern int
htree_init(htree * tree);

extern void
htree_cleanup(htree * tree);

extern int
htree_put(htree * tree, struct hnode * node);

extern int
htree_put(htree * tree, const thash hash, const char * str);

extern struct hnode *
htree_pop(htree * tree, const thash hash);

extern int
htree_insert(htree * tree, const thash hash, const char * str);

extern int
htree_insert2(htree * tree, const thash hash, const char * str, const size_t size);

extern int
htree_remove(htree * tree, const thash hash, char ** str, const size_t size);

extern char *
htree_remove2(htree * tree, const thash hash);

extern int
htree_search(const htree * tree, const thash hash, char ** str, const size_t size);

extern char *
htree_search2(const htree * tree, const thash hash);

extern size_t
htree_length(const htree * tree, const thash hash);


#ifdef __cplusplus
}
#endif
  
#endif //HTREE_H
