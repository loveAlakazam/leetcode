from math import sqrt
#트리노드
class TreeNode:
    def __init__(self, point):
        self.left=None
        self.right=None
        self.p=point #점 좌표
        self.d=sqrt(point[0]**2+point[1]**2) #원점과의 거리
        
class BinarySearchTree:
    def __init__(self):
        self.root=None #이진탐색트리의 루트노드 -> 처음에는 없다고 가정한다.
        self.ans=[] #초기화
        
    def insert_node(self, point): #노드삽입
        #노드를 만든다
        new_node=TreeNode(point)
        
        #트리가 비어있다면
        if self.root is None:
            self.root=new_node
            
        #트리가 비어있지 않다면
        else:
            prev=None #now의 부모노드
            now=self.root
            while now: #현재노드가 존재한다면..
                prev= now
                
                # 새로만든 노드의 원점사이 거리가 now노드의 원점사이 거리보다 크거나 같다면
                if new_node.d >= now.d:
                    now= now.right
                # new_node.d < now.d
                else:
                    now= now.left
            if new_node.d>= prev.d:
                prev.right=new_node
            else: #new_node.d<prev.d
                prev.left=new_node  
    #전위순회
    def pre_order(self, node):
        if node: #노드가 존재한다면
            #왼쪽서브트리 탐색
            self.pre_order(node.left)
            
            #나자신 탐색
            self.ans.append(node.p)
            
            #오른쪽서브트리 탐색
            self.pre_order(node.right)
           
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        #이진탐색트리를 만든다.
        bst=BinarySearchTree()
        
        #points에 있는 원소들을가지고 노드를 삽입한다.
        for point in points:
            bst.insert_node(point)
        
        #전위순회
        bst.pre_order(bst.root)
        return bst.ans[:K]
