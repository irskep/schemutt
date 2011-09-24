Schemutt
========

Schemutt is an XML schema figure-outer. I wrote it to help me understand some undocumented APIs.

This script will run on Python 2.7 and 3.2.

Output Format
-------------

    filename
    <TagName>
      Attribute1 = {'attribute value 1', 'attribute value 2', ...}
      Attribute2 = {'attribute value 3', 'attribute value 4', ...}
      <ChildTag>
        ...

Example output:

    > python3 schemutt.py graph_data_example.xml
    graph_data_example.xml
    <GraphData>
      <GenericProcesses>
        <GenericProcess>
          GenericProcessID = {'018a3f66-4e5a-4746-947a-bb22242cffd4'}
          Reversible = {'True'}
          Name = {'alpha-D-Glucose 6-phosphate phosphohydrolase'}
          ID = {'4b681112-df3c-44c6-8eda-85f08a2ea9ae'}
          <Catalyzes>
            <Catalyze>
              OrganismGroupID = {'01bea179-c89d-42c7-9add-fbe807f46fe9'}
              GeneProductMoleculeID = {'e51a5e9c-0389-4a0e-b1f5-acb1817e7a2f'}
              ECNumber = {'1.2.7.1', '4.2.1.11', '4.1.1.49', '5.4.2.1'}
              ProcessID = {'596cd74b-16b4-49e4-8008-8a1956ff9a25'}
          <Molecules>
            <Molecule>
              ProcessID = {'596cd74b-16b4-49e4-8008-8a1956ff9a25'}
              Role = {'product', 'inhibitor', 'substrate', 'cofactor'}
              ID = {'346ccf50-0339-4a90-aca1-7ce3732f1663'}
      <Molecules>
        <Molecule>
          EntityID = {'5336ed04-0643-4687-afdd-afa008c9aca9'}
          IsCommon = {'False', 'True'}
          ID = {'2376e8fc-2b4a-4f4c-8784-2ee298918a69'}
          Name = {'Thiamin diphosphate'}
      <Pathways>
        <Pathway>
          Name = {'Pyruvate metabolism'}
          Expanded = {'True', 'False'}
          ID = {'9d3a7f76-8ad0-4c2c-ba59-ae912713d359'}
          Linking = {'False', 'True'}
          <LinkingPathways>
            <LinkingPathway>
              ID = {'9d3a7f76-8ad0-4c2c-ba59-ae912713d359'}
              Dir = {'out', 'in'}
              <LinkingMolecule>
                ID = {'9d51294b-c808-4c7b-86c5-bd446e2e51a9'}
          <OrganismGroups>
            <OrganismGroup>
              ID = {'01bea179-c89d-42c7-9add-fbe807f46fe9'}
          <GenericProcesses>
            <GenericProcess>
              ID = {'4b681112-df3c-44c6-8eda-85f08a2ea9ae'}
