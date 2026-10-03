## Date: 2026-09-09

### What I tried
- To detect if `ls` has been tampered with, I can run `dpkg -V coreutils` (or `dpkg -V | grep /bin/ls`). If the output shows a `5` next to `/bin/ls`, the checksum doesn't match the original package, meaning `ls` has been replaced. A clean system returns no output.

### What broke
-

### What I learned
- Attackers can hide their tracks by editing `~/.bash_history` directly, or by creating a fake 'normal' history and overwriting the file. The second method is stealthier because a completely empty history is suspicious, but a full history of boring commands is not.
- The sticky bit (`t`) on `/tmp` stops users from deleting files they don't own. But `root` is the exception — the system administrator can delete anything. This means the sticky bit protects normal users from each other, but it does not stop a root-level attacker.
- It's a good idea to make the name of list plural  as a list would normally contain more than one element, []
- Python considers first item in a list to be at position 0, not position 1. This has to do with how the list operations are implemented at a lower level. Accessing last elements use the index of  -1, second-to-last use -3 and so on. This is useful if we don't know how long exactly the list is.
- To add to a list, we use the append() which add the item to the end of the list. To insert at any position in the list, we use the insert(position_number, 'item'). To delete from the list, we use the del listName[] with the position to be deleted withing the square braackets. we could also use the pop() which removes the last item in the list and could also remove based on the item position, pop(2). 
- when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
- If you don't know the position of ehat you removing then usse the remove('item') method
- Sorting a list using the method sort, cars.sort() is permanent. We can use the function sorted(cars) to bypass this. to reverse the sort alphabetically, we do the cars.sort(reverse=True)
- The reverse method, cars.reverse() rearrange the list in reverse order. It doesn't sort.
- len() function finds the length of a list
- Index error means python can't find the item at the index you requested
- 
### Commands/code worth remembering
```code

```

### Questions for later
-