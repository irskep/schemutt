> schemutt --find-foreign-keys simple_example.xml
simple_example.xml
<PathwayLayout>
  <Nodes>
    <NodeLayout>
      Y = {'879.5694734042553', '876.2212021276594', '1079.5484000000001'}
      X = {'221.26220119148942', '1612.846808510638', '472.4837841702128'}
      ID = {'6054abb3-dc31-43a0-9bd6-b9dda7af77e5'}
        -> PathwayLayout.Edges.EdgeLayout/SourceID (87/94)
        -> PathwayLayout.Edges.EdgeLayout/TargetID (79/94)
        -> PathwayLayout.Edges.EdgeLayout/SourceNeighboringProcessId (27/94)
        -> PathwayLayout.Edges.EdgeLayout/TargetNeighboringProcessId (22/94)
      NeighboringProcessId = {'14fd303b-b106-4e7a-b51a-6d2f9b3d2805'}
                          -> PathwayLayout.Edges.EdgeLayout/TargetID (29/30)
                          -> PathwayLayout.Edges.EdgeLayout/SourceID (29/30)
                          -> PathwayLayout.Edges.EdgeLayout/SourceNeighboringProcessId (28/30)
                          -> PathwayLayout.Edges.EdgeLayout/TargetNeighboringProcessId (23/30)
      cofactor = {'i', ' ', 'c'}
              -> PathwayLayout.Edges.EdgeLayout/SourceCofactor (3/3)
  <Edges>
    <EdgeLayout>
      SourceID = {'6054abb3-dc31-43a0-9bd6-b9dda7af77e5'}
              -> PathwayLayout.Nodes.NodeLayout/ID (87/87)
              -> PathwayLayout.Nodes.NodeLayout/NeighboringProcessId (29/87)
      TargetCofactor = {' '}
      TargetID = {'c03a2447-fff2-4ef8-896c-65fd36be0ab8'}
              -> PathwayLayout.Nodes.NodeLayout/ID (79/79)
              -> PathwayLayout.Nodes.NodeLayout/NeighboringProcessId (29/79)
      SourceNeighboringProcessId = {'8c8b1006-b06e-4c59-9b1a-84df2c6d0faf'}
                                -> PathwayLayout.Nodes.NodeLayout/NeighboringProcessId (28/28)
                                -> PathwayLayout.Nodes.NodeLayout/ID (27/28)
      TargetNeighboringProcessId = {'14fd303b-b106-4e7a-b51a-6d2f9b3d2805'}
                                -> PathwayLayout.Nodes.NodeLayout/NeighboringProcessId (23/23)
                                -> PathwayLayout.Nodes.NodeLayout/ID (22/23)
      SourceCofactor = {'i', ' ', 'c'}
                    -> PathwayLayout.Nodes.NodeLayout/cofactor (3/3)
      <BendPoint>
        Y = {'1080.210644335484', '787.2429629629629', '683.8948148148148'}
        X = {'1379.7704548254878', '1378.709530510858', '1574.5530864197533'}
