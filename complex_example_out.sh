> schemutt --find-foreign-keys complex_example.xml
complex_example.xml
<GraphData>
  <GenericProcesses>
    <GenericProcess>
      GenericProcessID = {'018a3f66-4e5a-4746-947a-bb22242cffd4'}
      Reversible = {'True'}
      Name = {'alpha-D-Glucose 6-phosphate phosphohydrolase'}
      ID = {'6054abb3-dc31-43a0-9bd6-b9dda7af77e5'}
        -> GraphData.Pathways.Pathway.GenericProcesses.GenericProcess/ID (52/52)
      <Catalyzes>
        <Catalyze>
          OrganismGroupID = {'01bea179-c89d-42c7-9add-fbe807f46fe9'}
                         -> GraphData.Pathways.Pathway.OrganismGroups.OrganismGroup/ID (1412/1412)
          GeneProductMoleculeID = {'e51a5e9c-0389-4a0e-b1f5-acb1817e7a2f'}
                               -> GraphData.Molecules.Molecule/ID (21/21)
                               -> GraphData.Molecules.Molecule/EntityID (21/21)
          ECNumber = {'1.2.7.1', '4.2.1.11', '5.3.1.1', '1.2.1.59', '1.2.7.6'}
          ProcessID = {'596cd74b-16b4-49e4-8008-8a1956ff9a25'}
                   -> GraphData.GenericProcesses.GenericProcess.Molecules.Molecule/ProcessID (20/20)
      <Molecules>
        <Molecule>
          ProcessID = {'596cd74b-16b4-49e4-8008-8a1956ff9a25'}
                   -> GraphData.GenericProcesses.GenericProcess.Catalyzes.Catalyze/ProcessID (20/52)
          Role = {'product', 'inhibitor', 'substrate', 'cofactor'}
          ID = {'b3e4ee53-18f8-4e14-90ca-7d2441d7e2c7'}
            -> GraphData.Molecules.Molecule/ID (52/52)
            -> GraphData.Pathways.Pathway.LinkingPathways.LinkingPathway.LinkingMolecule/ID (32/52)
  <Molecules>
    <Molecule>
      EntityID = {'80fdd82b-8d4d-4669-abea-fa76f23fa7e8'}
              -> GraphData.GenericProcesses.GenericProcess.Catalyzes.Catalyze/GeneProductMoleculeID (21/73)
      IsCommon = {'True', 'False'}
      ID = {'d86f2eae-86aa-4ef5-a52b-8c091ad2cce0'}
        -> GraphData.GenericProcesses.GenericProcess.Molecules.Molecule/ID (52/73)
        -> GraphData.Pathways.Pathway.LinkingPathways.LinkingPathway.LinkingMolecule/ID (32/73)
        -> GraphData.GenericProcesses.GenericProcess.Catalyzes.Catalyze/GeneProductMoleculeID (21/73)
      Name = {'Reduced ferredoxin', 'GDP', '3-Phospho-D-glycerate', 'NADH'}
  <Pathways>
    <Pathway>
      Name = {'Pyruvate metabolism'}
      Expanded = {'False', 'True'}
      ID = {'9d3a7f76-8ad0-4c2c-ba59-ae912713d359'}
        -> GraphData.Pathways.Pathway.LinkingPathways.LinkingPathway/ID (31/32)
      Linking = {'True', 'False'}
      <LinkingPathways>
        <LinkingPathway>
          ID = {'c19f472a-2431-460d-b847-89dacefe8084'}
            -> GraphData.Pathways.Pathway/ID (31/31)
          Dir = {'in', 'out'}
          <LinkingMolecule>
            ID = {'3152204b-2844-4dc1-a227-a5b6550b1804'}
              -> GraphData.Molecules.Molecule/ID (32/46)
              -> GraphData.GenericProcesses.GenericProcess.Molecules.Molecule/ID (32/46)
      <OrganismGroups>
        <OrganismGroup>
          ID = {'01bea179-c89d-42c7-9add-fbe807f46fe9'}
            -> GraphData.GenericProcesses.GenericProcess.Catalyzes.Catalyze/OrganismGroupID (1412/1416)
      <GenericProcesses>
        <GenericProcess>
          ID = {'8c8b1006-b06e-4c59-9b1a-84df2c6d0faf'}
            -> GraphData.GenericProcesses.GenericProcess/ID (52/52)
