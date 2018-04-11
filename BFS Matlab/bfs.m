% return cell array with n_paths ordered by shortest lenght 
function [paths] = bfs(adjMatrix, startNode, targetNode)

%nodesWeights=[1 1 1 1 1 1 1 1 1 1 1 30 1 1 1 1 1 1 20 1 1 1 1 1 1];

visitedNodes= zeros(1,length(adjMatrix));

%enqueue start node
queue=startNode;
visitedNodes(startNode)=1; %mark start node as visited

path=zeros(1,length(adjMatrix));
lenPath=0;
countPaths=0;
paths={};
%BFS loop
while(~isempty(queue)) %&& allVisited(visitedNodes,targetNode)==0)
    u = queue(1);
    queue(1)=[];
    for v=1:length(visitedNodes)
        if (visitedNodes(v)==0&& (adjMatrix(u,v)>0))
        %enqueue v
        queue=[queue v];
        path(v)=u;
        
        visitedNodes(v)=visitedNodes(v)+1;

        if(v==targetNode)%if reached target, append a path to cell array of paths
            %visitedNodes(v)=visitedNodes(v)+1
            pathSequence=targetNode;
            node=targetNode;
            while (node~=startNode)
                %lenPath=lenPath+nodesWeights(node);
                pathSequence= [pathSequence path(node)];
                node = path(node);
            end
            cellPath=fliplr(pathSequence);
            %cellPath{2}=lenPath;
            if(~equalPath(paths,cellPath))
                countPaths=countPaths+1;
                paths{countPaths}=cellPath;
                
            end
            queue(length(queue))=[];
            %lenPath=0;
            visitedNodes(targetNode)=0;
        end
        end
    end
end %end of while. 

end