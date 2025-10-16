from familytree_class import FamilyTree
from familytree_database import family_tree
#Class for managing family members
class ImmediateFamily(FamilyTree):

    # Method to retrieve family members
    def get_immediate_family(self):
        member_name = input("Enter the name of the person: ").lower()
        if member_name not in family_tree:  # Check if the record of person exists in the tree
            print(f"No record of {member_name.capitalize()} found")
            return
        member = family_tree[member_name]

        # Retrieve information about parents, siblings, spouse, and children
        parents = self.get_parents(member_name) or []
        siblings = self.get_siblings(member_name) or []
        spouse = member.get_spouse() or []
        children = self.get_children(member_name) or []

        # Display family
        print(f"Immediate family of {member_name.capitalize()}:")
        print(f"Parents: {', '.join(parents) if parents else 'Not available.'}")
        print(f"Siblings: {', '.join(siblings) if siblings else 'No siblings.'}")
        print(f"Spouse: {', '.join(spouse) if spouse else 'No spouse.'}")
        print(f"Children: {', '.join(children) if children else 'No children.'}")

        # Method to retrieve extended family
    def get_extended_family(self, member_name):
        # Convert the input name to lowercase for consistent dictionary lookup
        member_name = member_name.lower()
        # Check if the person exists in the family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        member = family_tree[member_name]
        # Get parents and filter for living ones
        parents = [
            p for p in (self.get_parents(member_name) or [])
            if p and family_tree[p.lower()].get_death_year() is None]
        # Siblings and filter for living ones
        siblings = [
            s for s in (self.get_siblings(member_name) or [])
            if s and family_tree[s.lower()].get_death_year() is None]
        # Get spouse(s) and filter for living ones
        spouse = [
            sp for sp in (member.get_spouse() or [])
            if sp and family_tree[sp.lower()].get_death_year() is None]
        # Get children and filter for living ones
        children = [
            c for c in (self.get_children(member_name) or [])
            if c and family_tree[c.lower()].get_death_year() is None]
        # Find aunts and uncles and filter for living ones
        aunts_uncles = set()
        for parent in parents:
            aunts_uncles.update([
                s for s in self.get_siblings(parent.lower())
                if s.lower() != member_name and family_tree[s.lower()].get_death_year() is None])
        # Find cousins (children of the aunts and uncles) and filter for living ones
        cousins = set()
        for aunt_uncle in aunts_uncles:
            cousins.update([
                c for c in (self.get_children(aunt_uncle.lower()) or [])
                if family_tree[c.lower()].get_death_year() is None])
        # Organize the results for display
        family = {
            'Parents': sorted(parents),
            'Siblings': sorted(siblings),
            'Spouse': sorted(spouse),
            'Children': sorted(children),
            'Aunts/Uncles': sorted(aunts_uncles),
            'Cousins': sorted(cousins)}
        # Print the results
        print(f"Extended family of {member_name.capitalize()} (living only):")
        for relation, members in family.items():
            print(f"{relation}: {', '.join(m.capitalize() for m in members) if members else 'None'}")

