"""GotraDatabase with 49+ gotras and their origins/pravara."""
from __future__ import annotations
from ..models import Gotra


class GotraDatabase:
    """Database of 49+ gotras with their rishis, pravaras, and origins."""

    def __init__(self) -> None:
        self._gotras: list[Gotra] = self._load_gotras()

    def _load_gotras(self) -> list[Gotra]:
        return [
            Gotra(name="Bharadvaja", rishi="Bharadvaja", pravara=["Bharadvaja", "Brihaspati", "Angirasa"], veda="Rigveda", sutra="Ashvalayana", origin="Descendant of sage Brihaspati through Angirasa lineage", description="One of the Saptarishis. Bharadvaja was a great Vedic scholar and author of many hymns."),
            Gotra(name="Kashyapa", rishi="Kashyapa", pravara=["Kashyapa", "Avatsara", "Naidhruva"], veda="Rigveda", sutra="Ashvalayana", origin="Kashyapa is considered the father of all living beings", description="Progenitor of the devas, asuras, nagas, and all living creatures through his many wives."),
            Gotra(name="Vashishtha", rishi="Vashishtha", pravara=["Vashishtha", "Indrapramada", "Abharadhvasu"], veda="Rigveda", sutra="Ashvalayana", origin="One of the Saptarishis; guru of the Ikshvaku dynasty", description="The royal priest of the Solar dynasty. Known for possessing the divine cow Kamadhenu."),
            Gotra(name="Vishvamitra", rishi="Vishvamitra", pravara=["Vishvamitra", "Devarata", "Audala"], veda="Rigveda", sutra="Ashvalayana", origin="Born a Kshatriya king who became a Brahmarishi through penance", description="Creator of the Gayatri Mantra. His tapas rivaled that of Vashishtha."),
            Gotra(name="Gautama", rishi="Gautama", pravara=["Gautama", "Angirasa", "Ayasya"], veda="Rigveda/Samaveda", sutra="Various", origin="Son of sage Gotama, descendant of Angirasa", description="Known for discovering the principles of logic (Nyaya). His wife was Ahalya."),
            Gotra(name="Jamadagni", rishi="Jamadagni", pravara=["Jamadagni", "Bhargava", "Chyavana", "Apnavana", "Aurva"], veda="Rigveda", sutra="Ashvalayana", origin="Father of Parashurama, descended from Bhrigu", description="One of the Saptarishis. Known for his strict penance and the divine cow Surabhi."),
            Gotra(name="Atri", rishi="Atri", pravara=["Atri", "Archananas", "Shyavashva"], veda="Rigveda", sutra="Ashvalayana", origin="One of the mind-born sons of Brahma", description="One of the Saptarishis. His wife Anasuya was the embodiment of chastity. Parents of Dattatreya."),
            Gotra(name="Agastya", rishi="Agastya", pravara=["Agastya", "Dardachyuta", "Idhmavaha"], veda="Rigveda", sutra="Ashvalayana", origin="Born from a pot (Kumbhaja), son of Mitra and Varuna", description="The sage who brought Vedic culture to South India. Drank the ocean dry."),
            Gotra(name="Angirasa", rishi="Angirasa", pravara=["Angirasa", "Brihaspati", "Bharadvaja"], veda="Rigveda/Atharvaveda", sutra="Various", origin="One of the mind-born sons of Brahma", description="Progenitor of the Angirasa clan. Teacher of divine knowledge. Associated with Atharvaveda."),
            Gotra(name="Bhrigu", rishi="Bhrigu", pravara=["Bhrigu", "Chyavana", "Apnavana", "Aurva", "Jamadagni"], veda="Rigveda", sutra="Various", origin="One of the Prajapatis, born from Brahma's skin", description="Compiler of Bhrigu Samhita (Vedic astrology text). Father of Shukracharya."),
            Gotra(name="Kaushika", rishi="Vishvamitra (Kaushika)", pravara=["Vishvamitra", "Devarata", "Audala"], veda="Rigveda", sutra="Various", origin="Branch of Vishvamitra gotra, named after his clan name Kaushika", description="Vishvamitra was originally king Kaushika before becoming a rishi."),
            Gotra(name="Vatsa", rishi="Vatsa", pravara=["Vatsa", "Bhargava", "Chyavana", "Apnavana", "Aurva"], veda="Rigveda", sutra="Various", origin="Sub-lineage of Bhrigu gotra", description="Associated with the Bhrigu lineage. Known for scholarship and Vedic learning."),
            Gotra(name="Mudgala", rishi="Mudgala", pravara=["Mudgala", "Maudgalya", "Angirasa"], veda="Rigveda", sutra="Various", origin="Descendant of Angirasa through Bharadvaja", description="Known for his extreme poverty and generosity. A sub-branch of Bharadvaja."),
            Gotra(name="Sandilya", rishi="Sandilya", pravara=["Sandilya", "Asita", "Devala"], veda="Rigveda/Yajurveda", sutra="Various", origin="Descendant of Kashyapa", description="Known for Sandilya Bhakti Sutra. Associated with Yajurveda tradition."),
            Gotra(name="Kaundinya", rishi="Kaundinya", pravara=["Kaundinya", "Vashishtha", "Maitravaruna"], veda="Rigveda", sutra="Various", origin="Descendant of Vashishtha", description="First disciple of the Buddha in some traditions. Prominent in South Indian Brahmin lineages."),
            Gotra(name="Parasara", rishi="Parasara", pravara=["Parasara", "Vashishtha", "Shakti"], veda="Rigveda", sutra="Various", origin="Grandson of Vashishtha, father of Vyasa", description="Author of Vishnu Purana and Brihat Parasara Hora Shastra (astrology)."),
            Gotra(name="Garga", rishi="Garga", pravara=["Garga", "Bharadvaja", "Angirasa"], veda="Rigveda", sutra="Various", origin="Descendant of Bharadvaja", description="Known for Garga Samhita. The priest who named Krishna and Balarama."),
            Gotra(name="Harita", rishi="Harita", pravara=["Harita", "Angirasa", "Ambarisha"], veda="Rigveda", sutra="Various", origin="Descendant of Angirasa lineage", description="Author of Harita Smriti and Harita Dharmasutra."),
            Gotra(name="Maudgalya", rishi="Maudgalya", pravara=["Maudgalya", "Angirasa", "Bharadvaja"], veda="Rigveda", sutra="Various", origin="Descended from Mudgala through Angirasa lineage", description="Associated with the famous disciple Maudgalyayana of the Buddha."),
            Gotra(name="Srivatsa", rishi="Srivatsa", pravara=["Srivatsa", "Chyavana", "Bhargava"], veda="Rigveda", sutra="Various", origin="Branch of Bhrigu gotra", description="The Srivatsa mark is sacred to Vishnu. Common among South Indian Brahmins."),
            Gotra(name="Katyayana", rishi="Katyayana", pravara=["Katyayana", "Vishvamitra", "Devarata"], veda="Yajurveda", sutra="Katyayana", origin="Descended from Vishvamitra", description="Author of important Sanskrit grammar works and Shrauta Sutra."),
            Gotra(name="Shaunaka", rishi="Shaunaka", pravara=["Shaunaka", "Gritsamada", "Bhargava"], veda="Atharvaveda", sutra="Shaunaka", origin="Descendant of Shunaka through Bhrigu lineage", description="Compiler of the Rigveda Padapatha. Head of Naimisharanya ashram."),
            Gotra(name="Lohita", rishi="Lohita", pravara=["Lohita", "Vashishtha", "Indrapramada"], veda="Rigveda", sutra="Various", origin="Sub-branch of Vashishtha gotra", description="Found among Brahmin communities in various parts of India."),
            Gotra(name="Dhananjaya", rishi="Dhananjaya", pravara=["Dhananjaya", "Vashishtha", "Parashara"], veda="Rigveda", sutra="Various", origin="Branch of Vashishtha-Parashara lineage", description="Named after the sage Dhananjaya of the Vashishtha clan."),
            Gotra(name="Shandilya", rishi="Shandilya", pravara=["Shandilya", "Asita", "Devala"], veda="Yajurveda", sutra="Various", origin="Descendant of Kashyapa through Asita", description="Variant spelling of Sandilya. Common in eastern Indian Brahmin families."),
            Gotra(name="Naidhruva", rishi="Naidhruva Kashyapa", pravara=["Kashyapa", "Avatsara", "Naidhruva"], veda="Rigveda", sutra="Various", origin="Sub-lineage of Kashyapa gotra through Naidhruva", description="Branch of the Kashyapa gotra with distinct pravara."),
            Gotra(name="Kanva", rishi="Kanva", pravara=["Kanva", "Ghora", "Apnuvana"], veda="Yajurveda", sutra="Kanva Shukla Yajurveda", origin="Important recension of Yajurveda named after him", description="Foster father of Shakuntala. His ashram was in the Malavara region."),
            Gotra(name="Kapisthala", rishi="Kapisthala", pravara=["Kapisthala", "Kashyapa", "Avatsara"], veda="Yajurveda", sutra="Kapisthala", origin="Branch of Kashyapa gotra associated with Krishna Yajurveda", description="Named after Kapisthala Katha Samhita of the Krishna Yajurveda."),
            Gotra(name="Manu", rishi="Manu", pravara=["Manu", "Aila", "Pururavas"], veda="Various", sutra="Various", origin="Manu is the progenitor of humankind", description="Related to the first lawgiver. Manusmriti is attributed to him."),
            Gotra(name="Mandavya", rishi="Mandavya", pravara=["Mandavya", "Bhargava", "Chyavana"], veda="Rigveda", sutra="Various", origin="Branch of Bhrigu gotra", description="Known from the story of Mandavya and the curse on Dharma (Vidura's birth)."),
            Gotra(name="Upamanyu", rishi="Upamanyu", pravara=["Upamanyu", "Vashishtha", "Indrapramada"], veda="Rigveda", sutra="Various", origin="Descendant of Vashishtha", description="Known from the Mahabharata as a great devotee of Shiva who taught Krishna."),
            Gotra(name="Marichi", rishi="Marichi", pravara=["Marichi", "Kashyapa", "Vatsara"], veda="Rigveda", sutra="Various", origin="One of the mind-born sons of Brahma, father of Kashyapa", description="Among the first Prajapatis created by Brahma."),
            Gotra(name="Pulaha", rishi="Pulaha", pravara=["Pulaha", "Viswaksena", "Jatukarnya"], veda="Various", sutra="Various", origin="One of the mind-born sons of Brahma", description="One of the seven great sages. Associated with creation of animals."),
            Gotra(name="Pulastya", rishi="Pulastya", pravara=["Pulastya", "Agastya", "Vishrava"], veda="Various", sutra="Various", origin="Mind-born son of Brahma, grandfather of Ravana", description="Through his son Vishrava, grandfather of Ravana and Kubera."),
            Gotra(name="Kratu", rishi="Kratu", pravara=["Kratu", "Sanaka", "Sanandana"], veda="Various", sutra="Various", origin="One of the Saptarishis in some lists", description="Known for great sacrificial knowledge. Performed major yajnas."),
            Gotra(name="Dalabhya", rishi="Dalabhya", pravara=["Dalabhya", "Saunaka", "Bhargava"], veda="Atharvaveda", sutra="Various", origin="Branch of Shaunaka through Bhrigu lineage", description="Associated with Atharvaveda tradition."),
            Gotra(name="Darbha", rishi="Darbha", pravara=["Darbha", "Kashyapa", "Avatsara"], veda="Various", sutra="Various", origin="Branch of Kashyapa gotra", description="Named after the sacred darbha grass used in rituals."),
            Gotra(name="Kutsa", rishi="Kutsa", pravara=["Kutsa", "Angirasa", "Mandhatri"], veda="Rigveda", sutra="Various", origin="Friend of Indra, Angirasa descendant", description="Featured in Rigvedic hymns as a companion of Indra in defeating Asuras."),
            Gotra(name="Bhardwaj", rishi="Bharadvaja", pravara=["Bharadvaja", "Brihaspati", "Angirasa"], veda="Rigveda", sutra="Ashvalayana", origin="Variant spelling of Bharadvaja", description="Same as Bharadvaja gotra; common variant spelling."),
            Gotra(name="Kapi", rishi="Kapi", pravara=["Kapi", "Angirasa", "Amahiyava"], veda="Rigveda", sutra="Various", origin="Descendant of Angirasa", description="Ancient gotra associated with the Angirasa lineage."),
            Gotra(name="Koushika", rishi="Vishvamitra (Koushika)", pravara=["Vishvamitra", "Devarata", "Audala"], veda="Rigveda", sutra="Various", origin="Variant of Kaushika", description="Same as Kaushika gotra; southern Indian spelling variant."),
            Gotra(name="Jabali", rishi="Jabali", pravara=["Jabali", "Gautama", "Angirasa"], veda="Rigveda", sutra="Various", origin="Branch of Gautama gotra", description="Known from the Ramayana as the sage who counseled Rama."),
            Gotra(name="Kasyapa", rishi="Kashyapa", pravara=["Kashyapa", "Avatsara", "Naidhruva"], veda="Rigveda", sutra="Various", origin="Variant spelling of Kashyapa", description="Same as Kashyapa gotra; alternate transliteration."),
            Gotra(name="Aupamanyava", rishi="Aupamanyava", pravara=["Aupamanyava", "Vashishtha", "Indrapramada"], veda="Rigveda", sutra="Various", origin="Descended from Upamanyu of Vashishtha line", description="Sub-branch of Vashishtha gotra through Upamanyu."),
            Gotra(name="Galava", rishi="Galava", pravara=["Galava", "Vishvamitra", "Devarata"], veda="Rigveda", sutra="Various", origin="Disciple of Vishvamitra", description="Known from Mahabharata. Gifted the divine horse Madhavi."),
            Gotra(name="Savarna", rishi="Savarna", pravara=["Savarna", "Kashyapa", "Avatsara"], veda="Various", sutra="Various", origin="Branch of Kashyapa", description="Associated with the concept of equal varna in some traditions."),
            Gotra(name="Maitreya", rishi="Maitreya", pravara=["Maitreya", "Kaundinya", "Vashishtha"], veda="Rigveda", sutra="Various", origin="Descended from Kaundinya-Vashishtha lineage", description="Known as a disciple of Parasara in the Vishnu Purana."),
            Gotra(name="Vatula", rishi="Vatula", pravara=["Vatula", "Kashyapa", "Avatsara"], veda="Various", sutra="Various", origin="Branch of Kashyapa gotra", description="Found among South Indian Brahmin communities."),
            Gotra(name="Kaashyapa", rishi="Kashyapa", pravara=["Kashyapa", "Avatsara", "Asita"], veda="Rigveda", sutra="Various", origin="Variant of Kashyapa with different pravara chain", description="Some Kashyapa sub-branches use Asita in pravara instead of Naidhruva."),
        ]

    def get_all_gotras(self) -> list[Gotra]:
        return self._gotras

    def get_gotra(self, name: str) -> Gotra | None:
        for g in self._gotras:
            if g.name.lower() == name.lower():
                return g
        return None

    def search_gotras(self, query: str) -> list[Gotra]:
        q = query.lower()
        return [g for g in self._gotras if q in g.name.lower() or q in g.rishi.lower()
                or q in g.description.lower()]

    def get_gotras_by_veda(self, veda: str) -> list[Gotra]:
        v = veda.lower()
        return [g for g in self._gotras if v in g.veda.lower()]

    def get_gotra_count(self) -> int:
        return len(self._gotras)
