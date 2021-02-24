'''
Recursive:
Case1.
p is None && q is None -> return True

Case2. 
p is None || q is None -> return False

Case3. 
p.val != q.val -> return False

Case4. 
isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
----

Example:
p = [1,2,3] , q = [1,2,3]
isSameTree(1,1)
isSameTree(2,2) and isSameTree(3,3)
isSameTree(None,None) and isSameTree(None,None)
'''
def isSameTree(p, q):
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)