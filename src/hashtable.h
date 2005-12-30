
struct hashtable_bucket
{
  int hash;
  char *key;
  void *value;
};


struct hashtable 
{
  int size; /* length of buckets array */
  int count; /* number of items (full buckets) in the hashtable */
  struct hashtable_bucket *buckets;
};

extern struct hashtable *hashtable_new(int initial_size);

extern void *hashtable_put(struct hashtable *table, char *key, void *value);

extern void *hashtable_get(struct hashtable *table, char *key);

extern void hashtable_print(FILE *f, struct hashtable *table);

extern void hashtable_iterate(struct hashtable *table, void func(void));
