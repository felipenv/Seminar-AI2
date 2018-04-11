% return cell array with n_paths ordered by shortest lenght 
function [paths] = dfs(adjMatrix, startNode, targetNode)

%enqueue start node
nodesWeights=[1 1 1 1 1 1 1 1 1 1 1 30 1 1 1 1 1 1 20 1 1 1 1 1 1];
visitedNodes= zeros(1,length(adjMatrix));

stack=startNode;
visitedNodes(startNode)=1; %mark start node as visited

path=zeros(1,length(adjMatrix));
lenPath=0;
countPaths=0;
paths={};
%BFS loop
while(length(stack)>0) %&& allVisited(visitedNodes,targetNode)==0)
    u = stack(length(stack));
    stack(length(stack))=[];
    for v=1:length(visitedNodes)
        if (visitedNodes(v)==0&& (adjMatrix(u,v)>0))
        %enqueue v
        stack=[stack v];
        path(v)=u;
        
        visitedNodes(v)=visitedNodes(v)+1;

        if(v==targetNode)%if reached target, append a path to cell array of paths
            %visitedNodes(v)=visitedNodes(v)+1
            pathSequence=targetNode;
            node=targetNode;
            while (node~=startNode)
                lenPath=lenPath+nodesWeights(node);
                pathSequence= [pathSequence path(node)];
                node = path(node);
            end
            cellPath={fliplr(pathSequence),lenPath};
            if(~equalPath(paths,cellPath{1}))
                countPaths=countPaths+1;
                paths{countPaths}=cellPath{1};
                
            end
            stack(length(stack))=[];
            lenPath=0;
            visitedNodes(targetNode)=0;
        end
        
        end
        visitedNodes(targetNode)=0; %to allow new path to be found
    end
    
end %end of while. 

end