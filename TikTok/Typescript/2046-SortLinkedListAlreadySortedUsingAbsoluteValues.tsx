/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function sortLinkedList(head: ListNode | null): ListNode | null {
    // Case 1 [0]
    // Case 2 [0, 2]
    // Case 3 [0, -2]
    // Case 4 [0, 2, -5, 5]
    let prev = head
    let node = head.next

    while (node !== null) {
        let next_node = node.next
        if (node.val < 0) {
            node.next = head
            head = node
            prev.next = next_node
        } else {
            prev = prev.next
        }
        node = next_node
    }
    return head
};