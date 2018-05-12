% return cell array with n_paths ordered by shortest lenght 
function [bestPath, waitingNodes] = A_star(adjMatrix, startNode, targetNode,stepNumber,paths_bots)

%enqueue start node
queue=startNode;
v_best=startNode;
distances=inf(1,length(adjMatrix));
path=zeros(1,length(adjMatrix));
waitingNodes=zeros(1,length(adjMatrix));
%stepNumber=0;
limit=10;
%A-star loop
while(v_best~=targetNode) %&& allVisited(visitedNodes,targetNode)==0)
    u = queue(1);
    stepNumber=stepNumber+1; %count current step of the path

    queue(1)=[]; %remove first element of the queue
    %check all nodes v that are reachable from current node u
    for v=1:length(adjMatrix)
        if (adjMatrix(u,v)>0)
            %check node with best improvement in path
            distances(v)=A_heuristics(v, targetNode, paths_bots, stepNumber);
        end
    end
    [minimum,v_best]=min(distances); %get index of array distances which is best next node
    %enqueue v_best
    queue=[queue v_best];

    if v_best~=u
        path(v_best)=u;
    else
        waitingNodes(v_best)=waitingNodes(v_best)+1;
    end
    distances=inf(1,length(adjMatrix));

    %reconstruct path found
    if(v_best==targetNode)%if reached target, append a path to cell array of paths
        pathSequence=targetNode;
        node=targetNode;
        stepSize=0;
        while (node~=startNode&&stepSize<limit) %loop to reconstruct path backing track
            %lenPath=lenPath+nodesWeights(node);
            pathSequence= [pathSequence path(node)];
            node = path(node);
            stepSize=stepSize+1;
            
        end
        bestPath=fliplr(pathSequence); %flip path to get in correct order
        
    end
        
end %end of while. 

end