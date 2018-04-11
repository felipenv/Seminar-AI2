%check if all nodes were visited except the target node 
function [allVisited] = allVisited(visitedNodes,targetNode)
    k = find(~visitedNodes);

    if k == targetNode
       allVisited=1  ;
    else
       allVisited=0;
    end
end