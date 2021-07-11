# include <queue>
using namespace std;

class MedianFinder {
public:
    priority_queue <int, deque<int>, less<int> > first_half;
    priority_queue <int, vector<int>, greater<int> > last_half;
    
    /** initialize your data structure here. */
    MedianFinder() {

    }
    
    void addNum(int num) {
        int first_num = first_half.size();
        int last_num = last_half.size();

        if (first_num == 0) {
            first_half.push(num);
            return ;
        }
    
        if (num <= first_half.top()){
            if (first_num - last_num == 1){
                last_half.push(first_half.top());
                first_half.pop();
            }

            first_half.push(num);
            return ; 
        }
        
        if (first_num - last_num == 0){
            if (last_half.top() > num) {
                first_half.push(num);
                return ;
            }
            
            first_half.push(last_half.top());
            last_half.pop();
            }
        
        last_half.push(num);
        
        return ;
    }
    
    double findMedian() {
        if (first_half.size() == last_half.size()){
            return (double)(first_half.top() + last_half.top()) / 2;
        }
        return (double)first_half.top();
    }
};
