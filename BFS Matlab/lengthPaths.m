function [lengthPaths] = lengthPaths(nodesWeights, paths)
    lengthPaths=[];
    for i=1:length(paths)
        len=0;
        for j=1:length(paths{i})
            len=len+nodesWeights(paths{i}(j));
        end
        lengthPaths=[lengthPaths len];
        
    end
        

end