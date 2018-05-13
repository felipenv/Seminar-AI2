function [full_path] = A_findPath(ozoseq,nodesWeights,adjMatrix,operations,paths_bots)
ozoseq
full_path=[];
%find paths using A-star
for i=1:operations+1
    %set step number correctly to not reset count
    if length(full_path)==0
        stepNumber=1;
    else
        stepNumber=length(full_path);
    end
    
    path=A_star(adjMatrix, ozoseq(i), ozoseq(i+1),stepNumber,paths_bots);
    
    for j=1:nodesWeights(ozoseq(i+1))-2
        path = [path ozoseq(i+1)];       
    end
    full_path=[full_path path];
end
full_path;
end